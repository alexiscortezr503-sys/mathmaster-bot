"""
Handlers principales — MathMaster Bot v2
"""
from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from data.database import upsert_user, get_user, get_stats, get_leaderboard, add_xp, log_exercise, log_exam
from exercises.engine import generate, check
from topics.content import get as get_content
from utils.keyboards import main_menu, topic_menu, topic_actions, after_exercise, back, TOPICS
from config import XP_EXERCISE_CORRECT, XP_EXERCISE_NO_HINT, XP_EXAM_PER_CORRECT, EXAM_QUESTIONS

WAIT_ANSWER = 1
WAIT_EXAM   = 2

# ─────────────────────────────────────────────────────────────────────────────
# /start
# ─────────────────────────────────────────────────────────────────────────────
async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    upsert_user(u.id, u.username or "", u.first_name)
    db = get_user(u.id)
    streak = db.get("streak", 0)
    streak_txt = f"🔥 Racha: *{streak} día{'s' if streak!=1 else ''}*\n" if streak > 1 else ""

    text = (
        f"🧮 *¡Bienvenido a MathMaster, {u.first_name}!*\n\n"
        f"{streak_txt}"
        f"Aprende matemáticas desde *Primaria hasta Licenciatura*.\n\n"
        f"Cada tema incluye:\n"
        f"✅ Teoría con ejemplos paso a paso\n"
        f"✏️ Ejercicios con corrección automática\n"
        f"📝 Exámenes de 5 preguntas con calificación\n"
        f"⭐ Sistema de XP y ranking global\n\n"
        f"👇 *Elige tu nivel:*"
    )
    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=main_menu())
    else:
        await update.callback_query.edit_message_text(text, parse_mode="Markdown", reply_markup=main_menu())

# ─────────────────────────────────────────────────────────────────────────────
# Callback router principal
# ─────────────────────────────────────────────────────────────────────────────
async def on_button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    d = q.data

    # Inicio
    if d == "inicio":
        await cmd_start(update, ctx)

    # Nivel → lista de temas
    elif d.startswith("lvl_"):
        level = d[4:]
        lvl_names = {"primaria":"🏫 Primaria","secundaria":"📚 Secundaria","universidad":"🎓 Universidad"}
        await q.edit_message_text(
            f"{lvl_names.get(level,'📚')} — *Elige un tema:*",
            parse_mode="Markdown", reply_markup=topic_menu(level)
        )

    # Tema → teoría + botones
    elif d.startswith("topic_"):
        _, level, topic = d.split("_", 2)
        content = get_content(level, topic)
        if content:
            await q.edit_message_text(content, parse_mode="Markdown", reply_markup=topic_actions(level, topic))
        else:
            await q.edit_message_text(
                f"📚 *Tema en construcción...*\n¡Pero ya puedes practicar!",
                parse_mode="Markdown", reply_markup=topic_actions(level, topic)
            )

    # Ejercicio — ex_{level}_{topic}_{difficulty}
    elif d.startswith("ex_"):
        parts = d.split("_")
        # ex_primaria_suma_resta_1  → parts = ['ex','primaria','suma','resta','1']
        difficulty = int(parts[-1])
        level  = parts[1]
        topic  = "_".join(parts[2:-1])
        await _send_exercise(q, ctx, level, topic, difficulty)
        return WAIT_ANSWER

    # Pista
    elif d.startswith("hint_"):
        ex = ctx.user_data.get("ex")
        if ex:
            ctx.user_data["hints"] = ctx.user_data.get("hints", 0) + 1
            await q.answer(f"💡 {ex.get('hint','Sin pista disponible')}", show_alert=True)

    # Examen
    elif d.startswith("exam_"):
        _, level, topic = d.split("_", 2)
        await _start_exam(q, ctx, level, topic)
        return WAIT_EXAM

    # Progreso
    elif d == "progreso":
        await _show_progress(q, update.effective_user)

    # Ranking
    elif d == "ranking":
        await _show_ranking(q)


async def _send_exercise(target, ctx, level, topic, difficulty=1):
    ex = generate(level, topic, difficulty)
    ctx.user_data.update({"ex": ex, "level": level, "topic": topic,
                          "diff": difficulty, "hints": 0, "mode": "exercise"})
    diff_label = {1:"🟢 Fácil", 2:"🟡 Medio", 3:"🔴 Difícil"}.get(difficulty, "")
    text = (
        f"✏️ *Ejercicio* {diff_label}\n\n"
        f"📌 {ex['q']}\n\n"
        f"_Escribe tu respuesta en el chat_"
    )
    from telegram import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Markup
    kb = Markup([
        [Btn("💡 Pista", callback_data=f"hint_{level}_{topic}"),
         Btn("🏠 Inicio", callback_data="inicio")]
    ])
    if hasattr(target, 'edit_message_text'):
        await target.edit_message_text(text, parse_mode="Markdown", reply_markup=kb)
    else:
        await target.message.reply_text(text, parse_mode="Markdown", reply_markup=kb)


async def _start_exam(target, ctx, level, topic):
    questions = [generate(level, topic, 2) for _ in range(EXAM_QUESTIONS)]
    ctx.user_data.update({"exam_q": questions, "exam_idx": 0,
                          "exam_correct": 0, "level": level, "topic": topic, "mode": "exam"})
    await _send_exam_question(target, ctx)


async def _send_exam_question(target, ctx):
    idx   = ctx.user_data["exam_idx"]
    total = EXAM_QUESTIONS
    q     = ctx.user_data["exam_q"][idx]
    bar   = "▓"*(idx) + "░"*(total-idx)
    text  = (
        f"📝 *Examen — Pregunta {idx+1}/{total}*\n"
        f"`{bar}`\n\n"
        f"❓ {q['q']}\n\n"
        f"_Escribe tu respuesta:_"
    )
    from telegram import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Markup
    kb = Markup([[Btn("🏠 Cancelar", callback_data="inicio")]])
    if hasattr(target, 'edit_message_text'):
        await target.edit_message_text(text, parse_mode="Markdown", reply_markup=kb)
    else:
        await target.message.reply_text(text, parse_mode="Markdown", reply_markup=kb)


async def _show_progress(q, user):
    db    = get_user(user.id)
    stats = get_stats(user.id)
    xp    = db.get("xp", 0)
    streak= db.get("streak", 0)
    rank  = ("🥉 Principiante" if xp < 100 else
             "🥈 Intermedio"   if xp < 500 else
             "🥇 Avanzado"     if xp < 1500 else
             "💎 Experto")
    ex    = stats["ex"]
    exam  = stats["exam"]
    total = ex.get("total") or 0
    corr  = ex.get("correct") or 0
    pct   = round(corr/total*100,1) if total else 0

    text = (
        f"📊 *Tu Progreso — {user.first_name}*\n\n"
        f"⭐ XP: *{xp}* — {rank}\n"
        f"🔥 Racha actual: *{streak} día{'s' if streak!=1 else ''}*\n\n"
        f"✏️ *Ejercicios:*\n"
        f"  Intentados: {total} | Correctos: {int(corr or 0)} ({pct}%)\n\n"
        f"📝 *Exámenes:*\n"
        f"  Realizados: {int(exam.get('total') or 0)} | "
        f"Promedio: {round(exam.get('avg') or 0,1)}%\n"
    )
    await q.edit_message_text(text, parse_mode="Markdown", reply_markup=back())


async def _show_ranking(q):
    board = get_leaderboard(10)
    medals = ["🥇","🥈","🥉"] + ["🏅"]*7
    lines  = [f"{medals[i]} *{r['first_name']}* — {r['xp']} XP 🔥{r['streak']}"
              for i,r in enumerate(board)]
    text = "🏆 *Ranking Global — Top 10*\n\n" + "\n".join(lines) if lines else "🏆 Aún no hay jugadores."
    await q.edit_message_text(text, parse_mode="Markdown", reply_markup=back())


# ─────────────────────────────────────────────────────────────────────────────
# Respuestas de texto (ejercicios y exámenes)
# ─────────────────────────────────────────────────────────────────────────────
async def on_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    mode = ctx.user_data.get("mode")

    if mode == "exercise":
        return await _handle_exercise_answer(update, ctx)
    elif mode == "exam":
        return await _handle_exam_answer(update, ctx)
    else:
        await update.message.reply_text(
            "👇 Usa el menú para empezar:", reply_markup=main_menu()
        )


async def _handle_exercise_answer(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ex     = ctx.user_data.get("ex")
    level  = ctx.user_data.get("level","")
    topic  = ctx.user_data.get("topic","")
    hints  = ctx.user_data.get("hints", 0)
    uid    = update.effective_user.id
    ans    = update.message.text.strip()

    correct = check(ans, ex["a"], ex.get("alts", []))
    log_exercise(uid, f"{level}_{topic}", correct, hints)

    if correct:
        xp = XP_EXERCISE_CORRECT + (XP_EXERCISE_NO_HINT if hints == 0 else 0)
        add_xp(uid, xp)
        header = f"✅ *¡Correcto!* +{xp} XP ⭐\n\n"
    else:
        header = f"❌ *Incorrecto*\nTu respuesta: `{ans}`\nRespuesta: `{ex['a']}`\n\n"

    await update.message.reply_text(
        header + ex["proc"],
        parse_mode="Markdown",
        reply_markup=after_exercise(level, topic)
    )
    ctx.user_data.clear()
    return ConversationHandler.END


async def _handle_exam_answer(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    idx    = ctx.user_data["exam_idx"]
    q      = ctx.user_data["exam_q"][idx]
    ans    = update.message.text.strip()
    level  = ctx.user_data["level"]
    topic  = ctx.user_data["topic"]
    uid    = update.effective_user.id
    correct= check(ans, q["a"], q.get("alts",[]))

    if correct:
        ctx.user_data["exam_correct"] += 1
        fb = f"✅ ¡Correcto!\n\n{q['proc']}"
    else:
        fb = f"❌ Incorrecto\nRespuesta: `{q['a']}`\n\n{q['proc']}"

    ctx.user_data["exam_idx"] += 1

    if ctx.user_data["exam_idx"] >= EXAM_QUESTIONS:
        # Fin del examen
        score = ctx.user_data["exam_correct"]
        total = EXAM_QUESTIONS
        pct   = score/total*100
        log_exam(uid, level, topic, score, total)
        xp = score * XP_EXAM_PER_CORRECT
        add_xp(uid, xp)

        grade = ("🏆 ¡Sobresaliente!" if pct>=90 else
                 "⭐ ¡Muy bien!"      if pct>=70 else
                 "📚 Aprobado"        if pct>=50 else
                 "❌ Reprobado — ¡Estudia más!")

        from telegram import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Markup
        kb = Markup([
            [Btn("🔄 Repetir examen", callback_data=f"exam_{level}_{topic}"),
             Btn("📚 Repasar tema",   callback_data=f"topic_{level}_{topic}")],
            [Btn("🏠 Inicio",         callback_data="inicio")],
        ])

        result = (
            f"{fb}\n\n"
            f"━━━━━━━━━━━━━━━━━━━━\n"
            f"📋 *RESULTADO FINAL*\n"
            f"✅ {score}/{total} correctas ({pct:.0f}%)\n"
            f"{grade}\n"
            f"⭐ +{xp} XP ganados"
        )
        await update.message.reply_text(result, parse_mode="Markdown", reply_markup=kb)
        ctx.user_data.clear()
        return ConversationHandler.END
    else:
        await update.message.reply_text(fb, parse_mode="Markdown")
        await _send_exam_question(update, ctx)
        return WAIT_EXAM

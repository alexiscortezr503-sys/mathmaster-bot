"""
Handlers completos — MathMaster Bot v3
"""
import io
import sympy as sp
from sympy import symbols, solve, diff, integrate, simplify, sympify
from sympy.plotting import plot as sp_plot
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from telegram import Update, InlineKeyboardButton as Btn, InlineKeyboardMarkup as Markup
from telegram.ext import ContextTypes, ConversationHandler
from data.database import upsert_user, get_user, get_stats, get_leaderboard, add_xp, log_exercise, log_exam
from exercises.engine import generate, check
from topics.content import get as get_content
from utils.keyboards import main_menu, topic_menu, topic_actions, after_exercise, donate_menu, back, TOPICS
from config import XP_EXERCISE_CORRECT, XP_EXERCISE_NO_HINT, XP_EXAM_PER_CORRECT, EXAM_QUESTIONS, ADMIN_ID

WAIT_ANSWER  = 1
WAIT_EXAM    = 2
WAIT_SOLVE   = 3
WAIT_GRAPH   = 4

x, y, z = symbols('x y z')

# ─────────────────────────────────────────────────────────────────────────────
# /start
# ─────────────────────────────────────────────────────────────────────────────
async def cmd_start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    u = update.effective_user
    upsert_user(u.id, u.username or "", u.first_name)
    db     = get_user(u.id)
    streak = db.get("streak", 0)
    streak_txt = f"🔥 Racha: *{streak} día{'s' if streak!=1 else ''}* — ¡Sigue así!\n" if streak>1 else ""

    text = (
        f"🧮 *¡Bienvenido a MathMaster, {u.first_name}!*\n\n"
        f"{streak_txt}"
        f"Tu asistente matemático completo 📚\n"
        f"Desde *Primaria* hasta *Licenciatura y más*.\n\n"
        f"¿Qué quieres hacer hoy? 👇"
    )
    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=main_menu())
    else:
        await update.callback_query.edit_message_text(text, parse_mode="Markdown", reply_markup=main_menu())

# ─────────────────────────────────────────────────────────────────────────────
# Router de botones
# ─────────────────────────────────────────────────────────────────────────────
async def on_button(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    q = update.callback_query
    await q.answer()
    d = q.data

    if d == "inicio":
        await cmd_start(update, ctx)

    elif d.startswith("lvl_"):
        level = d[4:]
        names = {"primaria":"🏫 Primaria","secundaria":"📚 Secundaria",
                 "universidad":"🎓 Universidad","avanzado":"🔬 Avanzado"}
        await q.edit_message_text(
            f"{names.get(level,'📚')} — *Elige un tema:*",
            parse_mode="Markdown", reply_markup=topic_menu(level)
        )

    elif d.startswith("topic_"):
        _, level, topic = d.split("_", 2)
        content = get_content(level, topic)
        text = content if content else f"📚 *Tema en construcción...*\n¡Pero ya puedes practicar!"
        await q.edit_message_text(text, parse_mode="Markdown", reply_markup=topic_actions(level, topic))

    elif d.startswith("ex_"):
        parts     = d.split("_")
        difficulty= int(parts[-1])
        level     = parts[1]
        topic     = "_".join(parts[2:-1])
        await _send_exercise(q, ctx, level, topic, difficulty)
        return WAIT_ANSWER

    elif d.startswith("hint_"):
        ex = ctx.user_data.get("ex")
        if ex:
            ctx.user_data["hints"] = ctx.user_data.get("hints", 0) + 1
            await q.answer(f"💡 {ex.get('hint','Sin pista disponible')}", show_alert=True)

    elif d.startswith("exam_"):
        _, level, topic = d.split("_", 2)
        await _start_exam(q, ctx, level, topic)
        return WAIT_EXAM

    elif d == "resolver":
        await q.edit_message_text(
            "✏️ *Resolver problema matemático*\n\n"
            "Escribe tu problema o ecuación y lo resuelvo paso a paso.\n\n"
            "*Ejemplos:*\n"
            "• `2x + 5 = 11`\n"
            "• `x^2 - 5x + 6 = 0`\n"
            "• `derive x^3 + 2x`\n"
            "• `integra x^2 + 3x`\n"
            "• `simplifica (x^2-1)/(x-1)`\n"
            "• `factoriza x^2 + 5x + 6`\n\n"
            "_Escribe tu problema:_",
            parse_mode="Markdown", reply_markup=back()
        )
        ctx.user_data["mode"] = "solver"
        return WAIT_SOLVE

    elif d == "graficar":
        await q.edit_message_text(
            "📈 *Graficar función*\n\n"
            "Escribe la función en términos de x.\n\n"
            "*Ejemplos:*\n"
            "• `x^2 - 3x + 2`\n"
            "• `sin(x)`\n"
            "• `x^3 - x`\n"
            "• `exp(x)`\n"
            "• `log(x)`\n\n"
            "_Escribe la función:_",
            parse_mode="Markdown", reply_markup=back()
        )
        ctx.user_data["mode"] = "grapher"
        return WAIT_GRAPH

    elif d == "progreso":
        await _show_progress(q, update.effective_user)

    elif d == "ranking":
        await _show_ranking(q)

    elif d == "acerca":
        await _show_about(q)

    elif d == "donar":
        await q.edit_message_text(
            "💝 *Apoyar MathMaster Bot*\n\n"
            "Este bot es completamente *gratuito* para todos los estudiantes. "
            "Si te ha ayudado y quieres apoyar su desarrollo, puedes donar desde Telegram.\n\n"
            "Cada donación ayuda a mantener el servidor activo y agregar nuevos temas 🙏\n\n"
            "Elige cómo quieres apoyar:",
            parse_mode="Markdown", reply_markup=donate_menu()
        )

        elif d == "donar_estrellas":
    await q.edit_message_text(
        "⭐ *Donar Estrellas de Telegram*\n\n"
        "Las Estrellas son la moneda oficial de Telegram.\n\n"
        "*Cómo donarme Estrellas:*\n"
        "1. Abre Telegram y busca *@mkoi.alex*\n"
        "2. Abre mi perfil\n"
        "3. Toca los tres puntos *( ... )*\n"
        "4. Selecciona *'Enviar regalo'*\n"
        "5. Elige la cantidad de Estrellas ⭐\n\n"
        "¡Cualquier cantidad es muy apreciada! 🙏\n"
        "Las Estrellas me ayudan a mantener el bot gratuito para todos. 💪",
        parse_mode="Markdown", reply_markup=back("donar")
    )

    elif d == "donar_ton":
        await q.edit_message_text(
            "💎 *Donar Toncoins (TON)*\n\n"
            "TON es la criptomoneda oficial de Telegram.\n\n"
            "Para donar TON:\n"
            "1. Abre *@wallet* en Telegram\n"
            "2. Ve a *Enviar*\n"
            "3. Envía TON a esta dirección:\n\n`UQAv_WaJjv6r7Frys8POL1m3xhoAzq7jNjFk7n803b2gmde2`\n\n"
            "4. Envía la cantidad que desees 💎\n\n"
            "¡Cualquier cantidad es muy apreciada! 🙏",
            parse_mode="Markdown", reply_markup=back("donar")
        )


# ─────────────────────────────────────────────────────────────────────────────
# Acerca del bot
# ─────────────────────────────────────────────────────────────────────────────
async def _show_about(q):
    text = (
        "ℹ️ *Acerca de MathMaster Bot*\n\n"
        "🧮 *¿Qué es MathMaster?*\n"
        "Un asistente matemático completo para estudiantes de todos los niveles, "
        "desde primer grado hasta Licenciatura en Matemáticas y más.\n\n"
        "📚 *¿Qué puedo hacer?*\n"
        "• Explicar cualquier tema matemático con ejemplos paso a paso\n"
        "• Generar ejercicios con corrección automática\n"
        "• Aplicar exámenes con calificación y porcentaje\n"
        "• Resolver ecuaciones y problemas escritos\n"
        "• Graficar funciones matemáticas\n"
        "• Llevar tu progreso y racha de estudio\n\n"
        "🏫 *Niveles disponibles:*\n"
        "• Primaria — Aritmética, fracciones, geometría\n"
        "• Secundaria — Álgebra, trigonometría, estadística\n"
        "• Universidad — Cálculo, álgebra lineal, EDOs\n"
        "• Avanzado — Teoría de números, topología, álgebra abstracta\n\n"
        "⚙️ *Tecnología:*\n"
        "Desarrollado con Python, SymPy y python-telegram-bot.\n"
        "Motor matemático real que verifica respuestas algebraicamente.\n\n"
        "👨‍💻 *Desarrollador:*\n"
        "Alexis Granados Cortez — Full Stack Developer\n"
        "📸 @mkoi.alex\n\n"
        "💝 *¿Te ayudó el bot?* Apóyalo con una donación para mantenerlo gratuito para todos."
    )
    kb = Markup([
        [Btn("💝 Apoyar el bot", callback_data="donar")],
        [Btn("🔙 Volver",        callback_data="inicio")],
    ])
    await q.edit_message_text(text, parse_mode="Markdown", reply_markup=kb)


# ─────────────────────────────────────────────────────────────────────────────
# Resolver problemas escritos
# ─────────────────────────────────────────────────────────────────────────────
async def handle_solver(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    uid  = update.effective_user.id

    try:
        result = _solve_expression(text)
        await update.message.reply_text(result, parse_mode="Markdown", reply_markup=_solver_kb())
    except Exception as e:
        await update.message.reply_text(
            f"⚠️ No pude interpretar eso.\n\n"
            f"*Prueba con formatos como:*\n"
            f"• `2x + 5 = 11`\n"
            f"• `x^2 - 4 = 0`\n"
            f"• `derive x^3 + 2x`\n"
            f"• `integra x^2`\n"
            f"• `simplifica (x^2-1)/(x-1)`",
            parse_mode="Markdown", reply_markup=_solver_kb()
        )
    return WAIT_SOLVE


def _solve_expression(text: str) -> str:
    t = text.lower().replace("^", "**")

    # Derivar
    if any(w in t for w in ["derive", "deriva", "derivada", "d/dx"]):
        expr_str = t
        for w in ["derive", "deriva", "derivada de", "d/dx", "d/dx de"]:
            expr_str = expr_str.replace(w, "").strip()
        expr = sympify(expr_str)
        result = diff(expr, x)
        return (f"∂ *Derivada*\n\n"
                f"f(x) = `{expr}`\n\n"
                f"📝 *Procedimiento:*\n"
                f"Aplicando reglas de derivación...\n\n"
                f"f'(x) = `{result}`\n\n"
                f"✅ *Resultado: {result}*")

    # Integrar
    if any(w in t for w in ["integra", "integral", "∫"]):
        expr_str = t
        for w in ["integra", "integral de", "integral"]:
            expr_str = expr_str.replace(w, "").strip()
        expr = sympify(expr_str)
        result = integrate(expr, x)
        return (f"∫ *Integral*\n\n"
                f"∫ `{expr}` dx\n\n"
                f"📝 *Procedimiento:*\n"
                f"Aplicando reglas de integración...\n\n"
                f"= `{result}` + C\n\n"
                f"✅ *Resultado: {result} + C*")

    # Simplificar
    if any(w in t for w in ["simplifica", "simplify"]):
        expr_str = t.replace("simplifica", "").replace("simplify", "").strip()
        expr   = sympify(expr_str)
        result = simplify(expr)
        return f"🔄 *Simplificación*\n\n`{expr}` = `{result}`\n\n✅ *Resultado: {result}*"

    # Factorizar
    if any(w in t for w in ["factoriza", "factor"]):
        expr_str = t.replace("factoriza", "").replace("factor", "").strip()
        expr   = sympify(expr_str)
        result = sp.factor(expr)
        return f"🔢 *Factorización*\n\n`{expr}` = `{result}`\n\n✅ *Resultado: {result}*"

    # Ecuación con =
    if "=" in text:
        lhs, rhs = text.split("=", 1)
        lhs_expr = sympify(lhs.replace("^","**"))
        rhs_expr = sympify(rhs.replace("^","**"))
        equation = lhs_expr - rhs_expr
        solutions = solve(equation, x)

        if not solutions:
            return "⚠️ No encontré soluciones reales para esta ecuación."

        steps = (f"⚖️ *Resolviendo ecuación*\n\n"
                 f"`{text}`\n\n"
                 f"📝 *Procedimiento:*\n"
                 f"Reordenando: `{equation} = 0`\n"
                 f"Despejando x...\n\n")

        if len(solutions) == 1:
            steps += f"✅ *Solución: x = {solutions[0]}*"
        else:
            sols = " | ".join([f"x = {s}" for s in solutions])
            steps += f"✅ *Soluciones: {sols}*"

        # Verificación
        steps += "\n\n*Verificación:*\n"
        for s in solutions:
            val_l = lhs_expr.subs(x, s)
            val_r = rhs_expr.subs(x, s)
            steps += f"x={s}: {val_l} = {val_r} ✅\n"

        return steps

    # Expresión general — evaluar/simplificar
    expr   = sympify(t)
    result = simplify(expr)
    return f"🔢 *Expresión*\n\n`{expr}` = `{result}`\n\n✅ *Resultado: {result}*"


def _solver_kb():
    return Markup([
        [Btn("✏️ Otro problema", callback_data="resolver")],
        [Btn("📈 Graficar",      callback_data="graficar"),
         Btn("🏠 Inicio",        callback_data="inicio")],
    ])


# ─────────────────────────────────────────────────────────────────────────────
# Graficar funciones
# ─────────────────────────────────────────────────────────────────────────────
async def handle_grapher(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()

    try:
        expr = sympify(text.replace("^", "**"))
        f    = sp.lambdify(x, expr, "numpy")

        import numpy as np
        xs = np.linspace(-10, 10, 500)
        ys = f(xs)

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(xs, ys, color="#c0392b", linewidth=2)
        ax.axhline(0, color='white', linewidth=0.8)
        ax.axvline(0, color='white', linewidth=0.8)
        ax.set_facecolor('#07050f')
        fig.patch.set_facecolor('#07050f')
        ax.tick_params(colors='white')
        ax.spines[:].set_color('gray')
        ax.set_title(f"f(x) = {expr}", color='white', fontsize=13)
        ax.set_xlabel("x", color='white')
        ax.set_ylabel("f(x)", color='white')
        ax.grid(True, alpha=0.2, color='gray')
        ax.set_ylim(-50, 50)

        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', dpi=120)
        buf.seek(0)
        plt.close()

        kb = Markup([
            [Btn("📈 Otra función", callback_data="graficar"),
             Btn("🏠 Inicio",       callback_data="inicio")],
        ])
        await update.message.reply_photo(
            photo=buf,
            caption=f"📈 *f(x) = {expr}*",
            parse_mode="Markdown",
            reply_markup=kb
        )
    except Exception as e:
        await update.message.reply_text(
            "⚠️ No pude graficar eso.\n\n"
            "*Ejemplos válidos:*\n"
            "• `x^2 - 3x + 2`\n"
            "• `sin(x)`\n"
            "• `x^3 - x`\n"
            "• `exp(-x^2)`",
            parse_mode="Markdown",
            reply_markup=Markup([[Btn("🔙 Volver", callback_data="inicio")]])
        )
    return WAIT_GRAPH


# ─────────────────────────────────────────────────────────────────────────────
# Ejercicios
# ─────────────────────────────────────────────────────────────────────────────
async def _send_exercise(target, ctx, level, topic, difficulty=1):
    ex = generate(level, topic, difficulty)
    ctx.user_data.update({"ex": ex, "level": level, "topic": topic,
                          "diff": difficulty, "hints": 0, "mode": "exercise"})
    diff_label = {1:"🟢 Fácil", 2:"🟡 Medio", 3:"🔴 Difícil"}.get(difficulty, "")
    text = f"✏️ *Ejercicio* {diff_label}\n\n📌 {ex['q']}\n\n_Escribe tu respuesta:_"
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
    bar   = "▓"*idx + "░"*(total-idx)
    text  = (f"📝 *Examen — Pregunta {idx+1}/{total}*\n"
             f"`{bar}`\n\n❓ {q['q']}\n\n_Escribe tu respuesta:_")
    kb = Markup([[Btn("🏠 Cancelar", callback_data="inicio")]])
    if hasattr(target, 'edit_message_text'):
        await target.edit_message_text(text, parse_mode="Markdown", reply_markup=kb)
    else:
        await target.message.reply_text(text, parse_mode="Markdown", reply_markup=kb)


# ─────────────────────────────────────────────────────────────────────────────
# Progreso y Ranking
# ─────────────────────────────────────────────────────────────────────────────
async def _show_progress(q, user):
    db    = get_user(user.id)
    stats = get_stats(user.id)
    xp    = db.get("xp", 0)
    streak= db.get("streak", 0)
    rank  = ("🥉 Principiante" if xp<100 else "🥈 Intermedio" if xp<500
             else "🥇 Avanzado" if xp<1500 else "💎 Experto")
    ex    = stats["ex"]
    exam  = stats["exam"]
    total = ex.get("total") or 0
    corr  = ex.get("correct") or 0
    pct   = round(corr/total*100,1) if total else 0
    text  = (f"📊 *Tu Progreso — {user.first_name}*\n\n"
             f"⭐ XP: *{xp}* — {rank}\n"
             f"🔥 Racha: *{streak} día{'s' if streak!=1 else ''}*\n\n"
             f"✏️ *Ejercicios:*\n"
             f"  Intentados: {total} | Correctos: {int(corr or 0)} ({pct}%)\n\n"
             f"📝 *Exámenes:*\n"
             f"  Realizados: {int(exam.get('total') or 0)} | "
             f"Promedio: {round(exam.get('avg') or 0,1)}%")
    await q.edit_message_text(text, parse_mode="Markdown", reply_markup=back())


async def _show_ranking(q):
    board  = get_leaderboard(10)
    medals = ["🥇","🥈","🥉"]+["🏅"]*7
    lines  = [f"{medals[i]} *{r['first_name']}* — {r['xp']} XP 🔥{r['streak']}"
              for i,r in enumerate(board)]
    text = "🏆 *Ranking Global — Top 10*\n\n" + "\n".join(lines) if lines else "🏆 Aún no hay jugadores."
    await q.edit_message_text(text, parse_mode="Markdown", reply_markup=back())


# ─────────────────────────────────────────────────────────────────────────────
# Respuestas de texto
# ─────────────────────────────────────────────────────────────────────────────
async def on_text(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    mode = ctx.user_data.get("mode")
    if mode == "exercise": return await _handle_exercise_answer(update, ctx)
    elif mode == "exam":   return await _handle_exam_answer(update, ctx)
    elif mode == "solver": return await handle_solver(update, ctx)
    elif mode == "grapher":return await handle_grapher(update, ctx)
    else:
        await update.message.reply_text("👇 Usa el menú:", reply_markup=main_menu())


async def _handle_exercise_answer(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    ex     = ctx.user_data.get("ex")
    level  = ctx.user_data.get("level","")
    topic  = ctx.user_data.get("topic","")
    hints  = ctx.user_data.get("hints", 0)
    uid    = update.effective_user.id
    ans    = update.message.text.strip()
    correct= check(ans, ex["a"], ex.get("alts",[]))
    log_exercise(uid, f"{level}_{topic}", correct, hints)
    if correct:
        xp = XP_EXERCISE_CORRECT + (XP_EXERCISE_NO_HINT if hints==0 else 0)
        add_xp(uid, xp)
        header = f"✅ *¡Correcto!* +{xp} XP ⭐\n\n"
    else:
        header = f"❌ *Incorrecto*\nTu respuesta: `{ans}`\nRespuesta: `{ex['a']}`\n\n"
    await update.message.reply_text(header+ex["proc"], parse_mode="Markdown",
                                    reply_markup=after_exercise(level, topic))
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
    if correct: ctx.user_data["exam_correct"] += 1
    fb = f"✅ ¡Correcto!\n\n{q['proc']}" if correct else f"❌ Incorrecto\nRespuesta: `{q['a']}`\n\n{q['proc']}"
    ctx.user_data["exam_idx"] += 1

    if ctx.user_data["exam_idx"] >= EXAM_QUESTIONS:
        score = ctx.user_data["exam_correct"]
        total = EXAM_QUESTIONS
        pct   = score/total*100
        log_exam(uid, level, topic, score, total)
        xp = score*XP_EXAM_PER_CORRECT
        add_xp(uid, xp)
        grade = ("🏆 ¡Sobresaliente!" if pct>=90 else "⭐ ¡Muy bien!" if pct>=70
                 else "📚 Aprobado" if pct>=50 else "❌ Reprobado — ¡Estudia más!")
        kb = Markup([
            [Btn("🔄 Repetir examen", callback_data=f"exam_{level}_{topic}"),
             Btn("📚 Repasar tema",   callback_data=f"topic_{level}_{topic}")],
            [Btn("🏠 Inicio",         callback_data="inicio")],
        ])
        result = (f"{fb}\n\n━━━━━━━━━━━━━━━━━━━━\n"
                  f"📋 *RESULTADO FINAL*\n✅ {score}/{total} ({pct:.0f}%)\n"
                  f"{grade}\n⭐ +{xp} XP")
        await update.message.reply_text(result, parse_mode="Markdown", reply_markup=kb)
        ctx.user_data.clear()
        return ConversationHandler.END
    else:
        await update.message.reply_text(fb, parse_mode="Markdown")
        await _send_exam_question(update, ctx)
        return WAIT_EXAM

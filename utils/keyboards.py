"""Teclados reutilizables para todo el bot"""
from telegram import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Markup

# ── Menú principal ────────────────────────────────────────────────────────────
def main_menu():
    return Markup([
        [Btn("🏫 Primaria",    callback_data="lvl_primaria"),
         Btn("📚 Secundaria",  callback_data="lvl_secundaria")],
        [Btn("🎓 Universidad", callback_data="lvl_universidad")],
        [Btn("🏆 Ranking",     callback_data="ranking"),
         Btn("📊 Mi progreso", callback_data="progreso")],
    ])

# ── Lista de temas por nivel ──────────────────────────────────────────────────
TOPICS = {
    "primaria": [
        ("➕ Suma y Resta",    "suma_resta"),
        ("✖️ Multiplicación", "multiplicacion"),
        ("➗ División",        "division"),
        ("½ Fracciones",      "fracciones"),
        ("📊 Porcentajes",    "porcentajes"),
        ("🔢 Decimales",      "decimales"),
    ],
    "secundaria": [
        ("📊 Álgebra",         "algebra"),
        ("⚖️ Ecuaciones 1°",  "ecuaciones"),
        ("📐 Cuadráticas",    "cuadraticas"),
        ("📐 Trigonometría",  "trigonometria"),
        ("🔢 Logaritmos",     "logaritmos"),
        ("🎲 Probabilidad",   "probabilidad"),
    ],
    "universidad": [
        ("∂ Cálculo Diferencial",       "calculo_diferencial"),
        ("∫ Cálculo Integral",          "calculo_integral"),
        ("🔢 Álgebra Lineal",           "algebra_lineal"),
        ("📉 Ec. Diferenciales",        "ecuaciones_diferenciales"),
    ],
}

def topic_menu(level: str):
    rows = []
    items = TOPICS.get(level, [])
    for i in range(0, len(items), 2):
        row = [Btn(items[i][0], callback_data=f"topic_{level}_{items[i][1]}")]
        if i+1 < len(items):
            row.append(Btn(items[i+1][0], callback_data=f"topic_{level}_{items[i+1][1]}"))
        rows.append(row)
    rows.append([Btn("🔙 Volver", callback_data="inicio")])
    return Markup(rows)

def topic_actions(level: str, topic: str):
    return Markup([
        [Btn("✏️ Practicar",  callback_data=f"ex_{level}_{topic}_1"),
         Btn("🔥 Difícil",    callback_data=f"ex_{level}_{topic}_3")],
        [Btn("📝 Examen (5 preguntas)", callback_data=f"exam_{level}_{topic}")],
        [Btn("🔙 Temas",      callback_data=f"lvl_{level}"),
         Btn("🏠 Inicio",     callback_data="inicio")],
    ])

def after_exercise(level: str, topic: str):
    return Markup([
        [Btn("🔄 Otro ejercicio",  callback_data=f"ex_{level}_{topic}_1"),
         Btn("🔥 Más difícil",     callback_data=f"ex_{level}_{topic}_3")],
        [Btn("📚 Ver teoría",      callback_data=f"topic_{level}_{topic}"),
         Btn("📝 Examen",          callback_data=f"exam_{level}_{topic}")],
        [Btn("🏠 Inicio",          callback_data="inicio")],
    ])

def back(dest="inicio"):
    return Markup([[Btn("🔙 Volver", callback_data=dest)]])

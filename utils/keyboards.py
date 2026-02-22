"""Teclados completos — MathMaster Bot v3"""
from telegram import InlineKeyboardButton as Btn, InlineKeyboardMarkup as Markup

def main_menu():
    return Markup([
        [Btn("🏫 Primaria",           callback_data="lvl_primaria"),
         Btn("📚 Secundaria",         callback_data="lvl_secundaria")],
        [Btn("🎓 Universidad",        callback_data="lvl_universidad"),
         Btn("🔬 Avanzado",           callback_data="lvl_avanzado")],
        [Btn("✏️ Resolver problema",  callback_data="resolver")],
        [Btn("📈 Graficar función",   callback_data="graficar")],
        [Btn("🏆 Ranking",            callback_data="ranking"),
         Btn("📊 Mi progreso",        callback_data="progreso")],
        [Btn("ℹ️ Acerca del bot",     callback_data="acerca"),
         Btn("💝 Apoyar el bot",      callback_data="donar")],
    ])

TOPICS = {
    "primaria": [
        ("➕ Suma y Resta",        "suma_resta"),
        ("✖️ Multiplicación",     "multiplicacion"),
        ("➗ División",            "division"),
        ("½ Fracciones",          "fracciones"),
        ("📊 Porcentajes",        "porcentajes"),
        ("🔢 Decimales",          "decimales"),
        ("📐 Geometría Básica",   "geometria_basica"),
        ("🧩 Problemas Lógica",   "problemas_logica"),
    ],
    "secundaria": [
        ("📊 Álgebra",             "algebra"),
        ("⚖️ Ecuaciones 1°",      "ecuaciones"),
        ("📐 Cuadráticas",        "cuadraticas"),
        ("📐 Trigonometría",      "trigonometria"),
        ("🔢 Logaritmos",         "logaritmos"),
        ("🎲 Probabilidad",       "probabilidad"),
        ("📈 Funciones",          "funciones"),
        ("🔷 Geometría Analítica","geometria_analitica"),
        ("🔢 Números Complejos",  "numeros_complejos"),
        ("📊 Estadística",        "estadistica"),
    ],
    "universidad": [
        ("∂ Cálculo Diferencial",       "calculo_diferencial"),
        ("∫ Cálculo Integral",          "calculo_integral"),
        ("🌐 Cálculo Multivariable",    "calculo_multivariable"),
        ("🔢 Álgebra Lineal",           "algebra_lineal"),
        ("📉 Ec. Diferenciales",        "ecuaciones_diferenciales"),
        ("📊 Estadística Inferencial",  "estadistica_inferencial"),
        ("🔬 Análisis Real",            "analisis_real"),
        ("💻 Matemática Discreta",      "matematica_discreta"),
    ],
    "avanzado": [
        ("🔢 Teoría de Números",        "teoria_numeros"),
        ("🔷 Topología",                "topologia"),
        ("⚛️ Álgebra Abstracta",       "algebra_abstracta"),
        ("🌊 Ec. Derivadas Parciales",  "edp"),
        ("📐 Geometría Diferencial",    "geometria_diferencial"),
        ("🔬 Análisis Complejo",        "analisis_complejo"),
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
        [Btn("✏️ Practicar",   callback_data=f"ex_{level}_{topic}_1"),
         Btn("🔥 Difícil",     callback_data=f"ex_{level}_{topic}_3")],
        [Btn("📝 Examen",      callback_data=f"exam_{level}_{topic}")],
        [Btn("🔙 Temas",       callback_data=f"lvl_{level}"),
         Btn("🏠 Inicio",      callback_data="inicio")],
    ])

def after_exercise(level: str, topic: str):
    return Markup([
        [Btn("🔄 Otro ejercicio", callback_data=f"ex_{level}_{topic}_1"),
         Btn("🔥 Más difícil",    callback_data=f"ex_{level}_{topic}_3")],
        [Btn("📚 Ver teoría",     callback_data=f"topic_{level}_{topic}"),
         Btn("📝 Examen",         callback_data=f"exam_{level}_{topic}")],
        [Btn("🏠 Inicio",         callback_data="inicio")],
    ])

def donate_menu():
    return Markup([
        [Btn("⭐ Donar Estrellas de Telegram", callback_data="donar_estrellas")],
        [Btn("💎 Donar Toncoins (TON)",        callback_data="donar_ton")],
        [Btn("🔙 Volver",                      callback_data="inicio")],
    ])

def back(dest="inicio"):
    return Markup([[Btn("🔙 Volver", callback_data=dest)]])

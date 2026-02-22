import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "TU_TOKEN_AQUI")
ADMIN_ID   = int(os.getenv("ADMIN_ID", "0"))

# XP por acción
XP_EXERCISE_CORRECT   = 15
XP_EXERCISE_NO_HINT   = 5   # bonus sin pista
XP_EXAM_PER_CORRECT   = 20
XP_STREAK_BONUS       = 10

EXAM_QUESTIONS = 5

LEVELS = {
    "primaria":    {"emoji": "🏫", "name": "Primaria (1° - 6°)"},
    "secundaria":  {"emoji": "📚", "name": "Secundaria / Bachillerato"},
    "universidad": {"emoji": "🎓", "name": "Universidad / Licenciatura"},
}

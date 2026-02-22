# 🧮 MathMaster Bot v2

Bot de Telegram para aprender matemáticas desde **1er grado hasta Licenciatura**.
Desarrollado por **Alexis Granados Cortez** — Full Stack Developer

---

## 🚀 Cómo subirlo a GitHub y hacerlo correr 24/7 en Railway

### PASO 1 — Sube el proyecto a GitHub

Abre la terminal (cmd o PowerShell) dentro de la carpeta del proyecto y ejecuta:

```bash
git init
git add .
git commit -m "MathMaster Bot v2 - Initial commit"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/mathmaster-bot.git
git push -u origin main
```
> Cambia `TU_USUARIO` por tu usuario de GitHub.
> Primero crea el repositorio vacío en github.com

---

### PASO 2 — Despliega en Railway (GRATIS, 24/7)

1. Ve a **https://railway.app** y regístrate con tu cuenta de GitHub
2. Haz clic en **"New Project"**
3. Selecciona **"Deploy from GitHub repo"**
4. Elige tu repositorio **mathmaster-bot**
5. Railway lo detecta automáticamente con el `Procfile`
6. Ve a la pestaña **"Variables"** y agrega:
   ```
   BOT_TOKEN = tu_token_de_telegram
   ADMIN_ID  = tu_id_de_telegram
   ```
7. Haz clic en **Deploy** ✅

¡Listo! Tu bot correrá **24/7 los 365 días del año** sin apagarse.

---

### PASO 3 — Probarlo localmente primero (opcional)

```bash
# 1. Crear entorno virtual
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Linux/Mac

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Crear archivo .env
cp .env.example .env
# Edita .env con tu token e ID

# 4. Correr el bot
python main.py
```

---

## 📁 Estructura del Proyecto

```
mathmaster_v2/
├── main.py              # Punto de entrada
├── config.py            # Configuración y tokens
├── requirements.txt     # Dependencias Python
├── Procfile             # Instrucciones para Railway
├── runtime.txt          # Versión de Python
├── .env.example         # Plantilla de variables
├── .gitignore
│
├── handlers/
│   └── main.py          # Todos los handlers del bot
│
├── topics/
│   └── content.py       # Teoría completa de todos los temas
│
├── exercises/
│   └── engine.py        # Motor de ejercicios + corrección con SymPy
│
├── data/
│   └── database.py      # SQLite — progreso, XP, streaks, ranking
│
└── utils/
    └── keyboards.py     # Todos los teclados del bot
```

---

## ✨ Funciones del Bot

| Función | Descripción |
|---------|-------------|
| 🏫 Primaria | Suma, resta, multiplicación, división, fracciones, porcentajes |
| 📚 Secundaria | Álgebra, ecuaciones, cuadráticas, trig, logaritmos |
| 🎓 Universidad | Cálculo diferencial, integral, álgebra lineal, EDOs |
| ✏️ Ejercicios | Generación aleatoria con 3 niveles de dificultad |
| 📝 Exámenes | 5 preguntas con calificación y porcentaje |
| ⭐ XP + Rachas | Sistema de puntos y racha diaria |
| 🏆 Ranking | Top 10 global de usuarios |
| 💡 Pistas | Ayuda en ejercicios sin spoilear |
| 🔢 Motor SymPy | Corrección matemática real (no solo comparar texto) |

---

## 🛠️ Stack Tecnológico

- **Python 3.11**
- **python-telegram-bot 21.x**
- **SymPy** — matemáticas simbólicas
- **SQLite** — base de datos local
- **Railway** — hosting 24/7 gratuito

---

## 📬 Contacto

- Instagram: [@mkoi.alex](https://instagram.com/mkoi.alex)
- Discord: cortez_503
- GitHub: [alexiscortezr503-sys](https://github.com/alexiscortezr503-sys)

import logging
from telegram.ext import (
    Application, CommandHandler, CallbackQueryHandler,
    MessageHandler, ConversationHandler, filters
)
from config import BOT_TOKEN
from data.database import init_db
from handlers.main import cmd_start, on_button, on_text, WAIT_ANSWER, WAIT_EXAM

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    level=logging.INFO
)

def main():
    init_db()
    app = Application.builder().token(BOT_TOKEN).build()
    conv = ConversationHandler(
        entry_points=[
            CallbackQueryHandler(on_button),
            CommandHandler("start", cmd_start),
        ],
        states={
            WAIT_ANSWER: [MessageHandler(filters.TEXT & ~filters.COMMAND, on_text)],
            WAIT_EXAM:   [MessageHandler(filters.TEXT & ~filters.COMMAND, on_text)],
        },
        fallbacks=[
            CommandHandler("start", cmd_start),
            CallbackQueryHandler(on_button),
        ],
        allow_reentry=True,
    )
    app.add_handler(conv)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, on_text))
    logging.info("🧮 MathMaster Bot v2 — Iniciado ✅")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()

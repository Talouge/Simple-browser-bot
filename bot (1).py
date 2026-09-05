import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# ==== Настройки ====
BOT_TOKEN = "ВАШ_ТОКЕН_ОТ_BOTFATHER"

DOWNLOAD_URL = "https://slmple.vercel.app/"
CHANNEL_URL = "https://t.me/SimpleBrowser"

START_TEXT = (
    "👋 Привет!\n\n"
    "Это бот браузера *Simple* — на Chromium, с адблоком, "
    "паролями и расширениями из коробки.\n\n"
    "Нажми кнопку ниже, чтобы скачать браузер или перейти в наш канал."
)


def main_keyboard() -> InlineKeyboardMarkup:
    keyboard = [
        [
            InlineKeyboardButton("📢 Наш канал", url=CHANNEL_URL),
            InlineKeyboardButton("⬇ Скачать Simple", url=DOWNLOAD_URL),
        ],
    ]
    return InlineKeyboardMarkup(keyboard)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        START_TEXT,
        parse_mode="Markdown",
        reply_markup=main_keyboard(),
        disable_web_page_preview=False,
    )


async def download(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отдельная команда /download на случай, если понадобится напрямую."""
    await update.message.reply_text(
        f"⬇ Скачать браузер Simple: {DOWNLOAD_URL}",
        reply_markup=main_keyboard(),
    )


async def channel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Отдельная команда /channel для перехода в канал."""
    await update.message.reply_text(
        f"📢 Наш канал: {CHANNEL_URL}",
        reply_markup=main_keyboard(),
    )


def main() -> None:
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("download", download))
    app.add_handler(CommandHandler("channel", channel))

    logger.info("Бот запущен")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()

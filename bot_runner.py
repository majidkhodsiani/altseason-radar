from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from config import TELEGRAM_TOKEN
from telegram_bot import show_portfolio


async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = show_portfolio()
    await update.message.reply_text(message)


def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    app.add_handler(
        CommandHandler("portfolio", portfolio)
    )

    print("Altseason Radar AI started")

    app.run_polling()


if __name__ == "__main__":
    main()

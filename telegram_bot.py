from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from bot import show_portfolio


async def portfolio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        show_portfolio()
    )


async def report(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = """
📊 گزارش Altseason Radar

سبد دریافت شد ✅

تحلیل کامل در حال آماده‌سازی است:
- RSI
- MACD
- واگرایی
- وضعیت نگهداری/فروش
"""
    await update.message.reply_text(message)


def start_bot(token):

    app = ApplicationBuilder().token(token).build()

    app.add_handler(
        CommandHandler("portfolio", portfolio)
    )

    app.add_handler(
        CommandHandler("report", report)
    )

    app.run_polling()

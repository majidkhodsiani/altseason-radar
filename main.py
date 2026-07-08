import os
from telegram_bot import start_bot


TOKEN = os.getenv("TELEGRAM_TOKEN")


if TOKEN:
    print("🤖 Altseason Radar started")
    start_bot(TOKEN)
else:
    print("❌ TELEGRAM_TOKEN not found")

import os
from telegram_bot import start_bot


TOKEN = os.getenv("TELEGRAM_TOKEN")


if __name__ == "__main__":

    if not TOKEN:
        print("Telegram token missing")
    else:
        start_bot(TOKEN)

import os

from dotenv import load_dotenv

load_dotenv()

bot_token = os.environ.get("BOT_TOKEN")
ai_token = os.environ.get("AI_TOKEN")


SQLALCHEMY_URL ="sqlite+aiosqlite:///db.sqlite3"
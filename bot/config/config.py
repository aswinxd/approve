import os
from dotenv import load_dotenv

load_dotenv("./.env")


class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2119246346:AAGrHWRcyCdNlKjcOypDtpkYbDhYTW0E7_Y")
    BOT_NAME = os.environ.get("BOT_NAME", "Bot")

    API_ID = int(os.environ.get("API_ID", "9927170"))
    API_HASH = os.environ.get("API_HASH", "37d90dc692d4412ea0209a4e34d20359")

    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://bot:bot@cluster0.8vepzds.mongodb.net/?retryWrites=true&w=majority")
    SESSION_NAME = os.environ.get("DATABASE_NAME", "TelegramBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002049466903"))
    SUDO_USERS = [int(user) for user in (os.environ.get("SUDO_USERS","6230751739 1877279215 5023815012 5906684391 5039863679")).split()]
    SUPPORT_CHAT_URL = os.environ.get("SUPPORT_CHAT_URL", "https://t.me/X1botchat")

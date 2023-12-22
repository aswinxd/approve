import os
from dotenv import load_dotenv

load_dotenv("./.env")


class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "2119246346:AAGrHWRcyCdNlKjcOypDtpkYbDhYTW0E7_Y")
    BOT_NAME = os.environ.get("BOT_NAME", "Aleena")

    API_ID = int(os.environ.get("API_ID", "27589257"))
    API_HASH = os.environ.get("API_HASH", "2119246346:AAGrHWRcyCdNlKjcOypDtpkYbDhYTW0E7_Y")

    DATABASE_URI = os.environ.get("DATABASE_URI", "mongodb+srv://bot:bot@cluster0.8vepzds.mongodb.net/?retryWrites=true&w=majority")
    SESSION_NAME = os.environ.get("DATABASE_NAME", "Aleena")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001696809539))
    SUDO_USERS = [int(user) for user in (os.environ.get("SUDO_USERS","")).split()]
    SUPPORT_CHAT_URL = os.environ.get("SUPPORT_CHAT_URL", "https://t.me/subotsupport")
  

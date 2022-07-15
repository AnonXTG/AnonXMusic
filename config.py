from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID", "4110592"))
API_HASH = getenv("API_HASH", "aa7c849566922168031b95212860ede0")
BOT_TOKEN = getenv("BOT_TOKEN", None)
BOT_NAME = getenv("BOT_NAME","YOURBOT_NAME")
BOT_USERNAME = getenv("BOT_USERNAME", "Jinx_music_bot")
OWNER_USERNAME = getenv("OWNER_USERNAME", "MAGNESIUM_XD")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "ArcaneXsupport")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
START_VID = getenv("START_VID", "https://telegra.ph/file/e28c02400d202c1e2d73d.mp4")
PING_IMG = getenv("PING_IMG", "https://telegra.ph/file/024d480ef4a670b0a93a0.jpg")
SESSION_NAME = getenv("SESSION_NAME", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "? ~ + • / ! ^ .").split())
PMPERMIT = getenv("PMPERMIT", "ENABLE")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))

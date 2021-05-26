import os
from base64 import b64decode

CLIENT_ID = os.getenv("DISCORD_TOKEN")
BOT_USER = os.getenv("BOT_USER")
# replit can't handle special characters...
BOT_PASSWORD = b64decode(os.getenv("BOT_PASSWORD").encode()).decode()
TEAM_HALO = "700383137670103101"

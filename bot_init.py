from discord.ext import commands

from constants import BOT_PASSWORD, BOT_USER, CLIENT_ID
from halo_api.auth import Auth
from halo_api.play import Play
from halo_api.users import Users

bot = commands.Bot(command_prefix="$", case_insensitive=True)


def attach_command(data, listener):
    return bot.command(name=data["command"], aliases=data.get("aliases", ()))(listener)


_auth = Auth(BOT_USER, BOT_PASSWORD).login()

play = Play(_auth)
users = Users(_auth)


def run():
    bot.run(CLIENT_ID)

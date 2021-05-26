import dotenv

dotenv.load_dotenv()

from cmd_listeners.top_users import top_users
from cmd_listeners.answer import answer
from cmd_listeners.disqualify import disqualify
from cmd_listeners.requalify import requalify
from cmd_listeners.user_details import user_details
from cmd_listeners.user_count import user_count
from cmd_listeners.graph import graph
from cmd_listeners.cipher import cipher
from cmd_listeners.decipher import decipher
from bot_init import run, attach_command


attach_command({"command": "top"}, top_users)
attach_command({"command": "answer"}, answer)
attach_command({"command": "disqualify", "aliases": ("dq",)}, disqualify)
attach_command({"command": "requalify", "aliases": ("rq",)}, requalify)
attach_command({"command": "user"}, user_details)
attach_command({"command": "count"}, user_count)
attach_command({"command": "graph"}, graph)
attach_command({"command": "cipher"}, cipher)
attach_command({"command": "decipher"}, decipher)


def init():
    print("Starting discord bot")
    run()


if __name__ == "__main__":
    init()

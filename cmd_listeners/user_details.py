from discord.ext import commands
from discord import Embed, Colour, AllowedMentions
from util.typing_indicator import send_typing_indicator
from datetime import datetime

from bot_init import users

mentions = AllowedMentions(everyone=False, roles=False)


async def user_details(ctx: commands.Context, user: str):
    message = await send_typing_indicator(ctx, "Fetching..")
    try:
        ret = users.user_details(user)
    except Exception as e:
        return await send_typing_indicator(ctx, f"Server error: {e}")
    await ctx.send(
        allowed_mentions=mentions,
        embed=Embed(
            title=f"{user} ({ret['name']})",
            colour=Colour.random(),
            description=f"**Lvl** {ret['level']}\n**Points** {ret['points']}\n**Account created at** {datetime.fromtimestamp(ret['created_at'])}",
        ),
    )
    await message.delete()

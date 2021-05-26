from util.is_team_halo import is_team_halo
from discord.ext import commands
from discord import AllowedMentions
from util.typing_indicator import send_typing_indicator


from bot_init import users


mentions = AllowedMentions(everyone=False, roles=False)


async def requalify(ctx: commands.Context, user: str):
    if not is_team_halo(ctx):
        return await send_typing_indicator(ctx, "https://quic.ml/pain")
    try:
        users.requalify(user)
    except Exception as e:
        return await send_typing_indicator(ctx, f"Server error: {e}")
    await ctx.send(f"Requalified {user}")

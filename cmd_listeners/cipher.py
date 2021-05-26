from util.is_team_halo import is_team_halo
from discord.ext import commands
from discord import AllowedMentions
from util.typing_indicator import send_typing_indicator
from cipher.encode import encode

from bot_init import users


mentions = AllowedMentions(everyone=False, roles=False)


async def cipher(ctx: commands.Context, *txt):
    if not is_team_halo(ctx):
        return await send_typing_indicator(ctx, "https://quic.ml/pain")
    try:
        return await send_typing_indicator(ctx,f'```{encode(" ".join(txt))}```')
    except Exception as e:
        return await send_typing_indicator(ctx,f"Server error: {e}")
    

from util.is_team_halo import is_team_halo
from discord.ext import commands
from discord import AllowedMentions
from util.typing_indicator import send_typing_indicator


from bot_init import play


mentions = AllowedMentions(everyone=False, roles=False)


async def answer(ctx: commands.Context, *args):
    if not is_team_halo(ctx):
        return await send_typing_indicator(ctx, "``` https://quic.ml/answer ```")
    if not args:
        return
    if len(args) == 2:
        event, question = args
    else:
        question = args[0]
        event = "main"
    message = await send_typing_indicator(ctx, "Fetching..")
    try:
        answer = play.get_answer(event, question)
    except Exception as e:
        return await send_typing_indicator(ctx, f"Server error: {e}")
    await ctx.send(allowed_mentions=mentions, content=f"``` {answer} ```")

    await message.delete()

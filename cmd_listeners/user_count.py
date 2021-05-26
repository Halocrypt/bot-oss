from discord.ext import commands
from discord import AllowedMentions
from util.typing_indicator import send_typing_indicator


from bot_init import play

mentions = AllowedMentions(everyone=False, roles=False)


async def user_count(ctx: commands.Context, *args):
    event = args[0] if args else "main"
    message = await send_typing_indicator(ctx, "Fetching..")
    try:
        count = play.get_user_count(event)
    except Exception as e:
        return await send_typing_indicator(ctx, f"Server error: {e}")
    await ctx.send(
        allowed_mentions=mentions,
        content=f"There are **{count}** members for the {event} event",
    )
    await message.delete()

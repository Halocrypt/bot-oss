from discord.ext import commands
from discord import Embed, Colour, AllowedMentions
from util.typing_indicator import send_typing_indicator


from bot_init import play

mentions = AllowedMentions(everyone=False, roles=False)


async def top_users(ctx: commands.Context, *args):
    event = args[0] if args else "main"
    message = await send_typing_indicator(ctx, "Fetching..")
    try:
        top_players = play.get_top_players(event)
    except Exception as e:

        return await send_typing_indicator(ctx, f"Server error: {e}")
    await ctx.send(
        allowed_mentions=mentions,
        embed=Embed(
            title="Top Players",
            colour=Colour.random(),
            description="\n".join(
                f"**{x['user']}** ({x['name']}) - Lvl {x['level']} ({x['points']} points)"
                for x in top_players
            ),
        ),
    )
    await message.delete()

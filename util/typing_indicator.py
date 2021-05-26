from asyncio import sleep
from discord.ext.commands import Context
from discord import Message


async def send_typing_indicator(ctx: Context, message: str, time=0.2) -> Message:
    await ctx.trigger_typing()
    await sleep(time)
    return await ctx.send(message)

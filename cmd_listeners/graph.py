from bot_init import users
from discord.ext import commands
from discord import AllowedMentions
import discord
from util.typing_indicator import send_typing_indicator
from datetime import datetime
import matplotlib.pyplot as plt

mentions = AllowedMentions(everyone=False, roles=False)


def get_time_str(a):
    x = datetime.fromtimestamp(a)
    return f"{x.day}-{x.month} ({x.hour}:{x.minute})"


async def graph(ctx: commands.Context, *args):
    message = await send_typing_indicator(ctx, "Fetching..")
    data = [i["created_at"] for i in users.get_all_users()]
    hours = []
    registrations = []
    current_hour = 0
    reg_count = 0
    data.sort()
    for i in data:
        if i - current_hour > 3600:
            current_hour = i
            hours.append(get_time_str(i))
            registrations.append(reg_count)
            reg_count = 0
        reg_count += 1

    fig: plt.Figure = plt.figure(figsize=(25, 7), tight_layout=True)

    ax: plt.Axes = fig.add_subplot(111)

    plt.xticks(rotation=45)
    ax.plot(hours, registrations)
    plt.savefig("chart.png", bbox_inches="tight")
    msg = discord.File("chart.png", filename="chart.png")
    embed = discord.Embed(
        title="chart", colour=discord.Colour(0x00FFBC), description=""
    )
    embed.set_image(url="attachment://chart.png")
    await ctx.send(allowed_mentions=mentions, file=msg, embed=embed)
    await message.delete()

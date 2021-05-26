import discord


async def delete(message: discord.Message):
    try:
        await message.delete()
    except:
        pass

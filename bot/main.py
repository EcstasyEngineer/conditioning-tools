from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix="/")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

bot.run(settings['discord']['token'])
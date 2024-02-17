import discord
from discord.ext.commands import Bot
import json
import os

intents = discord.Intents.default()
intents.messages = True  

bot = Bot(command_prefix='/', intents=intents)

with open('data/settings.json', 'r') as f:
    settings = json.load(f)

COGS = [
    'cogs.admin',
    'cogs.fun',
    'cogs.utils',
    'cogs.voice'
]

for cog in COGS:
    bot.load_extension(cog)

if __name__ == '__main__':
    TOKEN = settings['token']
    bot.run(TOKEN)

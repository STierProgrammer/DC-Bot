from bot.my_bot import bot
import json

with open('data/settings.json', 'r') as f:
    settings = json.load(f)
TOKEN = settings['token']

bot.run(TOKEN)

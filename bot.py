#bot.py
import os

import discord
import dotenv
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('discordToken')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

client.run(token)
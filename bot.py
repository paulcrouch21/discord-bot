#bot.py
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("discordToken")
guild = os.getenv("discordGuild")

bot = commands.Bot(command_prefix = "!")

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to my Discord server! Please check the info channel for the rules")

@bot.command(name = "99", help = "Responds with a random quote from Brooklyn 99")
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        "I\'m the human form of the 💯 emoji.",
        "Cool, cool cool cool cool. No doubt no doubt no doubt.",
        "A place where everybody knows your name is hell. You're describing hell.",
        "The English language can not fully capture the depth and complexity of my thoughts, so I’m incorporating emojis into my speech to better express myself. Winky face.",
        "If I die, turn my tweets into a book.",
        "I asked them if they wanted to embarrass you, and they instantly said yes.",
        "Good to see you. But if you’re here, who’s guarding Hades?"
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

bot.run(token)
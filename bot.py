#bot.py
import os
import random
import discord
from discord.ext import commands
from discord.utils import get
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("discordToken")
guild = os.getenv("discordGuild")
serverID = os.getenv('discordServerID')
welcome_byebyeID = os.getenv('welcome_byebye')

bot = commands.Bot(command_prefix = "!")
client = discord.Client()

@bot.event
async def on_ready():
    print(f"{bot.user.name} has connected to Discord!")

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hi {member.name}, welcome to the squad! Please check the info channel for the rules")
    role = get(member.guild.roles, name = 'Members')
    await member.add_roles(role)
    for channel in member.guild.channels:
        if str(channel) == "welcome_byebye":
            await channel.send(f"""Welcome to the squad, {member.mention}!""")

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

@bot.command(name = "naruto", help = "Responds with a random quote from the Naruto anime series")
async def naruto(ctx):
    naruto_quotes = [
        "I\'m not gonna run away, I never go back on my word! That’s my nindo: my ninja way.",
        "I care more about others than I do myself, and I won’t let anyone hurt them.",
        "My friends were the first to accept me for who I am.",
        "That\'s why we endure. We are ninja. I will never forget.",
        "Don’t underestimate me! I don’t quit and I don’t run.",
        "If you don’t like the hand that fate’s dealt you with, fight for a new one.",
        "Failing doesn’t give you a reason to give up, as long as you believe.",
        "Love breeds sacrifice, which in turn breeds hatred. Then you can know pain.",
        "Once you question your own belief it’s over.",
        "Hard work is worthless for those that don’t believe in themselves.",
        "When you give up, your dreams and everything else they’re gone.",
        "Never give up.",
        "It\'s not the face that makes someone a monster, it’s the choices they make with their lives.",
        "Before I became a ninja I was a nobody, but I never gave up."
    ]

    response = random.choice(naruto_quotes)
    await ctx.send(response)

bot.run(token)
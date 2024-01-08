import discord
from discord.ext import commands
import time
import random

some_id = random.randint(100000000011, 999999999999)
def ai(token, prefix=None):
    """
    ai(token, *prefix)
    token: Required, String
    prefix: Not Required, String
        - "!" as default

    Usage: ai("DISCORD_BOT_TOKEN", "PREFIX") or ai("DISCORD_BOT_TOKEN")
    Understands:
        prefix - hello
        prefix - ping

        More coming soon!
    """
    if prefix is None:
        a = "!"
    else:
        a = prefix
    b = token
    
    intents = discord.Intents.default()
    intents.message_content = True

    bot = commands.Bot(command_prefix=a, intents=intents)
    @bot.event
    async def on_ready():
        print("AI Bot is online!")
        channel = bot.get_channel(1163097696983339019)
        await channel.send(f"> ## {bot.user} was executed\n> * used package: new_ai.py\n> * Process time: {time.process_time()}\n> * Ping: {round(bot.latency * 1000)}ms")
        await bot.change_presence(activity=discord.Game(name=f'alpro.AI - {bot.user}'))
    @bot.command(description="Responds with hello and Pinging you")
    async def hello(ctx):
        await ctx.send(f'Hello, <@{ctx.author.id}>!')

    @bot.command(description="Shows the current ping and WebSocket ID of the bot\nBot's WebSocket ID changes everytime after rebooting")
    async def ping(ctx):
        await ctx.send(f'> Bot\'s Ping: {round(bot.latency * 1000)}ms\n> Bot\'s WebSocket id: {some_id}')


    bot.run(b)
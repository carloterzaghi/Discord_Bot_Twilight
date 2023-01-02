import discord
from discord.ext import commands
import os
import asyncio

bot = commands.Bot(command_prefix='!', intents= discord.Intents.all(), help_command= None)

@bot.event
async def on_ready():
    await bot.change_presence(
        status=discord.Status.idle, 
        activity= discord.Streaming(
            name= "Happy 2023!", 
            url= "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
            )
        )
    print(f"{bot.user.name} está online!")

async def load_cogs():
    for file in os.listdir("venv/commands"):
        if file.endswith(".py"):
            await bot.load_extension(f"commands.{file[:-3]}")

with open("./.env") as f:
    _token = f.read().strip()

async def main():      
    await load_cogs()
    await bot.start(_token)


if __name__ == "__main__":
    asyncio.run(main())
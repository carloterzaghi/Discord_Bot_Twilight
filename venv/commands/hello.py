import discord
from discord.ext import commands
from discord import app_commands

class hello(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"Synced {len(fmt)} command(s)")
    
    @app_commands.command(name='hello',description="Say hello")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Hello {interaction.user.mention}!")

async def setup(bot):
    await bot.add_cog(hello(bot))


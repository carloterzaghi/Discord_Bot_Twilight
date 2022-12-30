import discord
from discord.ext import commands
from discord import app_commands

class codeNames(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    @app_commands.command(name='rule',description="Bot game rules")
    async def rule(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title = "__CodeNames__",
            description= "*To start playing, select one of the two teams, blue or red.*\n"
        )
        embed.add_field(name= "\n__RULES__", value=
             "Two teams compete by each having a spymaster give one-word clues that " +
             "can point to multiple words on the board. The other players on the team attempt to guess " +
             "their team's words while avoiding the words of the other team."
             , inline=False)
        await interaction.response.send_message(embed= embed)
    
    @app_commands.command(name='play',description="Start a new game")
    async def play(self, interaction: discord.Interaction, OperativeRed : str, SpyMasterRed : str, OperativeBlue : str, SpyMasterBlue : str):

        embed = discord.Embed(
            title = "__CodeNames__",
            description= ""
        )
        embed.add_field(name= "\n__RED TEAM__", value=
             f"Operative: **{OperativeRed}**\nSpyMaster: **{SpyMasterRed}**"
             , inline=False)

        embed.add_field(name= "\n__BLUE TEAM__", value=
             f"Operative: **{OperativeBlue}**\nSpyMaster: **{SpyMasterBlue}**"
             , inline=False)
        await interaction.response.send_message(embed= embed)

async def setup(bot):
    await bot.add_cog(codeNames(bot))
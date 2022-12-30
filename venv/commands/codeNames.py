import discord
from discord.ext import commands
from discord import app_commands, ButtonStyle
from discord.ui import Button, View

class codeNames(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # Comando slash play
    @app_commands.command(name='play',description="Start a new game")
    async def play(self, interaction: discord.Interaction):

        blue_team =  Button(label= 'Blue Team', style= ButtonStyle.blurple)
        red_team =  Button(label= 'Red Team', style= ButtonStyle.red)
        blue = []
        red = []
        OperativeRed = []
        SpyMasterRed = []
        OperativeBlue = []
        SpyMasterBlue = []


        # Função do botão azul
        async def push_blue(interaction : discord.Interaction):
            if interaction.user.mention in blue:
                pass
            elif interaction.user.mention in red:
                red.remove(interaction.user.mention)
                blue.append(interaction.user.mention)
            else:
                blue.append(interaction.user.mention)

            blue_team =  Button(label= 'Blue Team', style= ButtonStyle.blurple)
            red_team =  Button(label= 'Red Team', style= ButtonStyle.red)

            embed = discord.Embed(
                title = "__CodeNames__",
                description= "*To start playing, select one of the two teams, blue or red.*\n"
            )
            embed.add_field(name= "\n__RULES__", value=
                "Two teams compete by each having a spymaster give one-word clues that " +
                "can point to multiple words on the board. The other players on the team attempt to guess " +
                "their team's words while avoiding the words of the other team."
                , inline=False)
            embed.add_field(name= "\n__TEAM__", value=
                "*The minimum to start is two players on each team.*\n"+
                f"**BLUE**: {blue}\n"+
                f"**RED**: {red}\n"
                , inline=False)

            blue_team.callback = push_blue
            red_team.callback = push_red

            proview = View(timeout=180)
            proview.add_item(blue_team)
            proview.add_item(red_team)

            if len(blue) >= 2 and len(red) >= 2:
                ready = Button(label= 'Ready', style= ButtonStyle.green)
                ready.callback = ready_push
                proview.add_item(ready)

            await interaction.response.edit_message(embed= embed, view= proview)

        # Função do botão vermelho
        async def push_red(interaction : discord.Interaction):
            if interaction.user.mention in red:
                pass
            elif interaction.user.mention in blue:
                blue.remove(interaction.user.mention)
                red.append(interaction.user.mention)
            else:
                red.append(interaction.user.mention)

            blue_team =  Button(label= 'Blue Team', style= ButtonStyle.blurple)
            red_team =  Button(label= 'Red Team', style= ButtonStyle.red)

            embed = discord.Embed(
                title = "__CodeNames__",
                description= "*To start playing, select one of the two teams, blue or red.*\n"
            )
            embed.add_field(name= "\n__RULES__", value=
                "Two teams compete by each having a spymaster give one-word clues that " +
                "can point to multiple words on the board. The other players on the team attempt to guess " +
                "their team's words while avoiding the words of the other team."
                , inline=False)
            embed.add_field(name= "\n__TEAM__", value=
                "*The minimum to start is two players on each team.*\n"+
                f"**BLUE**: {blue}\n"+
                f"**RED**: {red}\n"
                , inline=False)
                
            blue_team.callback = push_blue
            red_team.callback = push_red

            extraview = View(timeout=180)
            extraview.add_item(blue_team)
            extraview.add_item(red_team)

            if len(blue) >= 2 and len(red) >= 2:
                ready = Button(label= 'Ready', style= ButtonStyle.green)
                ready.callback = ready_push
                extraview.add_item(ready)

            await interaction.response.edit_message(embed= embed, view= extraview)

        # Função final do ready
        async def ready_push(interaction : discord.Interaction):

            operative =  Button(label= 'Operative', style= ButtonStyle.gray)
            spymaster =  Button(label= 'SpyMaster', style= ButtonStyle.grey)

            embed = discord.Embed(
                title = "__CodeNames__",
                description= 
                "*Before starting let's adjust the teams.*\n\n" +
                "*Select Operative or SpyMaster, minimum one in each class.*"
            )

            embed.add_field(name= "\n__BLUE TEAM__", value=
                f"Team: {blue}\nOperative: **{OperativeBlue}**\nSpyMaster: **{SpyMasterBlue}**"
                , inline=False)

            embed.add_field(name= "\n__RED TEAM__", value=
                f"Team: {red}\nOperative: **{OperativeRed}**\nSpyMaster: **{SpyMasterRed}**"
                , inline=False)

            operative.callback = operative_push
            spymaster.callback = spymaster_push

            proview = View(timeout=180)
            proview.add_item(operative)
            proview.add_item(spymaster)

            if len(blue)==(len(OperativeBlue)+len(SpyMasterBlue)) and len(red)==(len(OperativeRed)+len(SpyMasterRed)):
                ready = Button(label= 'Ready', style= ButtonStyle.green)
                ready.callback = game
                proview.add_item(ready)

            await interaction.response.edit_message(embed = embed,view = proview)

        # Push do botão Operative
        async def operative_push(interaction : discord.Interaction):
            if interaction.user.mention in blue:
                if interaction.user.mention in SpyMasterBlue:
                    OperativeBlue.append(interaction.user.mention)
                    SpyMasterBlue.remove(interaction.user.mention)
                elif interaction.user.mention in OperativeBlue:
                    pass
                else:
                    OperativeBlue.append(interaction.user.mention)
            elif interaction.user.mention in red:
                if interaction.user.mention in SpyMasterRed:
                    OperativeRed.append(interaction.user.mention)
                    SpyMasterRed.remove(interaction.user.mention)
                elif interaction.user.mention in OperativeRed:
                    pass
                else:
                    OperativeRed.append(interaction.user.mention)
            await ready_push(interaction)

        # Push do botão SpyMaster
        async def spymaster_push(interaction : discord.Interaction):
            if interaction.user.mention in blue:
                if interaction.user.mention in SpyMasterBlue:
                    pass
                elif interaction.user.mention in OperativeBlue:
                    OperativeBlue.remove(interaction.user.mention)
                    SpyMasterBlue.append(interaction.user.mention)
                else:
                    SpyMasterBlue.append(interaction.user.mention)
            elif interaction.user.mention in red:
                if interaction.user.mention in SpyMasterRed:
                    pass
                elif interaction.user.mention in OperativeRed:
                    OperativeRed.remove(interaction.user.mention)
                    SpyMasterRed.append(interaction.user.mention)
                else:
                    SpyMasterRed.append(interaction.user.mention)
            await ready_push(interaction)

        # Push do Ready dos times
        async def game(interaction : discord.Interaction):
            embed = discord.Embed(
                title = 'Fim de Jogo',
                color = 0x97CBFF
                )   
            proview = View(timeout=240)
            await interaction.response.edit_message(embed = embed,view = proview)


        blue_team.callback = push_blue
        red_team.callback = push_red

        myview = View(timeout=180)
        myview.add_item(blue_team)
        myview.add_item(red_team)

        embed = discord.Embed(
            title = "__CodeNames__",
            description= "*To start playing, select one of the two teams, blue or red.*\n"
        )
        embed.add_field(name= "\n__RULES__", value=
             "Two teams compete by each having a spymaster give one-word clues that " +
             "can point to multiple words on the board. The other players on the team attempt to guess " +
             "their team's words while avoiding the words of the other team."
             , inline=False)
        embed.add_field(name= "\n__TEAM__", value=
            "*The minimum to start is two players on each team.*\n"+
             f"**BLUE**: {blue}\n"+
             f"**RED**: {red}\n"
             , inline=False)
        await interaction.response.send_message(embed= embed, view= myview)
    

async def setup(bot):
    await bot.add_cog(codeNames(bot))
from discord.commands import SlashCommandGroup
from discord.ext import commands

class configCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    config = SlashCommandGroup("config", "Commands that allow you to control the bots configuration.")



def setup(bot):
    bot.add_cog(configCommands(bot))
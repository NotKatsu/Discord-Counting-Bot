from discord.commands import SlashCommandGroup
from discord.ext import commands

class messageEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


def setup(bot):
    bot.add_cog(messageEvents(bot))
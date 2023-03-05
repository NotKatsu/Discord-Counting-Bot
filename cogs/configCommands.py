import discord

from db import addChannel
from discord.ext import commands
from discord.commands import SlashCommandGroup


class configCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    config = SlashCommandGroup("config", "Commands that allow you to control the bots configuration.")


    @config.command() 
    async def channel(self, ctx, channel: discord.TextChannel): 
        addChannel(channel.id)


def setup(bot):
    bot.add_cog(configCommands(bot))
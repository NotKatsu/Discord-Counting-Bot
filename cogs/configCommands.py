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
        """Set the Counting Channel for members to count in."""
        if addChannel(channel) is True: 
            setChannel = discord.Embed(title="Set Counting Channel.",
                                    colour=discord.Colour(0xFAA61A),
                                    description=f"Set Counting channel to {channel.mention} `({channel.id})`")

            setChannel.set_footer(text=f"Channel Set • Counting Channel {channel.id}")
            await ctx.respond(embed=setChannel)
        else:
            Error = discord.Embed(title="Failed To Set Counting Channel.",
                                    colour=discord.Colour(0xFAA61A),
                                    description=f"I couldn't set the counting channel for this server.")

            Error.set_footer(text=f"Error • Could't Set Channel")
            await ctx.respond(embed=Error)


def setup(bot):
    bot.add_cog(configCommands(bot))
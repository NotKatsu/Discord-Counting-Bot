import discord

from db import addChannel
from discord.ext import commands
from discord.commands import SlashCommandGroup
from discord.ext.commands import has_permissions


class configCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    config = SlashCommandGroup("config", "Commands that allow you to control the bots configuration.")


    @config.command() 
    @has_permissions(manage_guild=True)
    async def channel(self, ctx, channel: discord.TextChannel): 
        """Set the Counting Channel for members to count in."""
        if addChannel(channel) is True: 
            setChannel = discord.Embed(title="Set Counting Channel.",
                                    colour=discord.Colour(0xFAA61A),
                                    description=f"Set Counting channel to {channel.mention} `({channel.id})`")

            setChannel.set_footer(text=f"Channel Set • Counting Channel {channel.id}")
            await ctx.respond(embed=setChannel)

            countingChannel = self.bot.get_channel(channel.id)
            await countingChannel.send(f":star: Counting channel has been set to this channel ({countingChannel.mention}). All you have to do is enter a number higher than the last number sent.\n\nWhoever wants to go first can just send the number **1**.")

        else:
            Error = discord.Embed(title="Failed To Set Counting Channel.",
                                    colour=discord.Colour(0xFAA61A),
                                    description=f"I couldn't set the counting channel for this server.")

            Error.set_footer(text=f"Error • Could't Set Channel")
            await ctx.respond(embed=Error)


def setup(bot):
    bot.add_cog(configCommands(bot))
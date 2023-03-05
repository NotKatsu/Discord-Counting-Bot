import discord

from db import addToCount
from discord.commands import SlashCommandGroup
from discord.ext import commands

class messageEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener() 
    async def on_message(self, message):
        addToCount(message)
        

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            missing_permissions = error.missing_permissions
            missingperms = discord.Embed(title=f" Missing Permissions",
                                         colour=discord.Colour(0xFAA61A),
                                         description=f"Sorry but you need the `{missing_permissions[0]}` permission to use that command.")

            await ctx.respond(embed=missingperms, ephemeral=True)


def setup(bot):
    bot.add_cog(messageEvents(bot))
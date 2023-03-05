import discord 
from discord.ext import commands 
from db import databaseSetup

bot = commands.Bot(status=discord.Status.online)


if __name__ == "__main__":
    if databaseSetup("database.db") == True: 
        extensions = ["cogs.messageEvents", "cogs.configCommands"]
        for extension in extensions:
            bot.load_extension(extension)
    else: 
        print("Database initialization failed");quit()

bot.run("MTA4MTk3MTI0Nzk3OTcwODQ4Nw.G6Zn8W.7mE_wWKdYEx4fw2XuY8d2_UqvWWOy5ZYlOW4Sc", reconnect=True)
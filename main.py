import os

import discord
from discord.ext import commands


# all commands will be of the form "!command-name" (or whatever prefix you choose)
bot = commands.Bot(command_prefix='!')


# name is the name you type on the server when you want to invoke the commmand
@bot.command(name='my-cool-command')
async def my_cool_command(context):
    # if you recall, a guild is just a fancy name for a server
    guild = str(context.guild)
    # now we print it in the terminal...
    print(guild)
    # ...and in the chat
    await context.send(guild)


def get_discord_bot_token():
    # tokens are usually passed to the script as environment variables
    # but you can also store them in a file (you will need to change this function)
    return os.getenv('DISCORD_TOKEN')


if __name__ == "__main__":
    token = get_discord_bot_token()
    bot.run(token)


import os

from discord.ext import commands
from pyjokes import get_joke

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


@bot.command(name='joke')
async def joke(context):
    joke = get_joke()
    await context.send(joke)


@bot.command()
async def reverse(context):
    print("processing !reverse")
    msg = context.message.content[9:]  # remove first 9 characters '!reverse '
    rev = msg[::-1]
    await context.send(rev)


@bot.event
async def on_message(message):
    if bot.user != message.author:
        if 'cat' in message.content:
            print('cat')
            await message.channel.send('cat')

    await bot.process_commands(message)

# @bot.event
# async def on_message(message):
#     if bot.user != message.author:
#         msg = f"well hi there {message.author.name}, thanks for saying '{message.content}'"
#         await message.channel.send(msg)


if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    print(token)
    print("running MYDBOT")
    bot.run(token)


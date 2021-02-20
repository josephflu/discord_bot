import os


from cog import Task
from discord.ext import commands, tasks
from pyjokes import get_joke

# all commands will be of the form "!command-name" (or whatever prefix you choose)
bot = commands.Bot(command_prefix='!')
#bot.add_cog(Task(bot))

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

@bot.command()
async def move(context):
    print("moving channel member")
    #move person over in channel
    all_channels = context.guild.voice_channels
    afkChannel = None
    for channel in all_channels:
        if 'AFK' in channel.name:
            afkChannel = channel
            break
    if afkChannel is None:
        print("AFK channel not found")
        return
    print("AFK channel found")
    user = context.message.author
    await user.move_to(afkChannel)
    #move user to AFK channel.


@bot.event
async def on_message(message):
    if bot.user != message.author:
        if 'cat' in message.content:
            print('cat')
            await message.channel.send('cat')

    await bot.process_commands(message)

@tasks.loop(seconds=3)
async def repeat():
    print("h  e  l  o")

    try:
        guild = bot.guilds[0]
        members = guild.members
        for vc in guild.voice_channels:
            if vc.name.startswith("AFK"):
                afk_channel = vc
                break
        for member in members:
            await member.move_to(afk_channel)
    except IndexError:
        print("The guilds list is empty now!")

# @bot.event
# async def on_message(message):
#     if bot.user != message.author:
#         msg = f"well hi there {message.author.name}, thanks for saying '{message.content}'"
#         await message.channel.send(msg)


if __name__ == "__main__":
    token = os.getenv('DISCORD_TOKEN')
    print(token)
    print("running MYDBOT")
    repeat.start()
    bot.run(token)


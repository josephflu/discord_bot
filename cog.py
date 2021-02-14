import discord.ext
from discord.ext import commands, tasks


class Task(commands.Cog):
    @tasks.loop(seconds=3)
    async def repeat(self):
        print("h  e  l  o")

        guild = self.bot.guilds[0]
        members = guild.members
        for vc in guild.voice_channels:
            if vc.name.startswith("AFK"):
                afk_channel = vc
                break
        for member in members:
            await member.move_to(afk_channel)




    def __init__(self, bot):
        self.repeat.start()
        self.bot = bot

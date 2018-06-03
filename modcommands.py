import discord
from discord.ext import commands
import asyncio
import random
from SwifflingBot import *

class ModCommands():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def mute(self, ctx):
        if "Mods" in [role.name for role in ctx.author.roles]:
            members = ctx.message.mentions
            for member in members:
                if "Mods" not in [role.name for role in member.roles]:
                    for ID in channels:
                        channel = client.get_channel(int(ID))
                        perms = discord.PermissionOverwrite()
                        perms.send_messages = False
                        await channel.set_permissions(member, overwrite=perms)
                    await ctx.send("{} has been muted".format(member.mention))
                else:
                    await ctx.send("You can't mute a fellow mod!")
        else:
            await ctx.send("You need to be a Mod to do this!")


    @commands.command(pass_context=True)
    async def unmute(self, ctx):
        if "Mods" in [role.name for role in ctx.author.roles]:
            members = ctx.message.mentions
            for member in members:
                if "Mods" not in [role.name for role in member.roles]:
                    for ID in channels:
                        channel = client.get_channel(int(ID))
                        await channel.set_permissions(member, overwrite=None)
                    await ctx.send("{} has been unmuted".format(member.mention))
                else:
                    await ctx.send("You can't unmute a fellow mod!")
        else:
            await ctx.send("You need to be a Mod to do this!")

    @commands.command(pass_context=True)
    async def open(self, ctx):
        if "The Switchlings" in [role.name for role in ctx.author.roles]:
            global permashut
            permashut = False
            await ctx.send("Should be open now")

    @commands.command(pass_context=True)
    async def lockdown(self, secs="indefinite"):
        if "The Switchlings" in [role.name for role in ctx.author.roles]:
            permashut = True
            try:
                secs = int(secs)
            except:
                pass
            for ID in channels:
                        channel = client.get_channel(int(ID))
                        perms = discord.PermissionOverwrite()
                        perms.send_messages = False
                        await channel.set_permissions(ctx.guild.default_role, overwrite=perms)
            await ctx.send("The Switchlings Plaza! is currently shut for lockdown.")
            if secs == "indefinite":
                while True:
                    await asyncio.sleep(1)
                    if permashut == False:
                        break
                    
            else:
                for i in range(0, secs):
                    await asyncio.sleep(1)
                    if permashut == False:
                        break
            for ID in channels:
                        channel = client.get_channel(int(ID))
                        perms = discord.PermissionOverwrite()
                        perms.send_messages = True
                        await channel.set_permissions(ctx.guild.default_role, overwrite=perms)
            await ctx.send("The Switchlings Plaza! is now open!")

    @commands.command(pass_context=True)
    async def timeout(self, timeouter: discord.Member, secs: int):
        if "Mods" in [role.name for role in ctx.author.roles]:
            if "Mods" not in [role.name for role in timeouter.roles]:
                 for ID in channels:
                   channel = client.get_channel(int(ID))
                   perms = discord.PermissionOverwrite()
                   perms.send_messages = False
                   await channel.set_permissions(timeouter, overwrite=perms)
                 await ctx.send("{} has been muted for {} seconds".format(timeouter.mention, secs))
                 for i in range(0, secs):
                    await asyncio.sleep(1)
                 for ID in channels:
                    channel = client.get_channel(int(ID))
                    await channel.set_permissions(timeouter, overwrite=None)
                 await ctx.send("{} has been unmuted after a timeout".format(timeouter.mention))
            else:
                await ctx.send("You cannot timeout a fellow mod!")
        else:
            await ctx.send("You need to be a Mod to do this!")

    @commands.command(pass_context=True)
    async def kick(self, ctx):
        kickers = ctx.message.mentions
        if "Mods" in [role.name for role in ctx.author.roles]:
            for kicker in kickers:
                if "Mods" in [role.name for role in kicker.roles]:
                    await ctx.send("You can't kick out a fellow Mod!")
                else:
                    await ctx.guild.kick(kicker)
                    await ctx.send("{} has been kicked".format(kicker.name))
        else:
            await ctx.send("You need to be a Mod to do this!")

    @commands.command(pass_context=True)
    async def ban(self, ctx):
        banners = ctx.message.mentions
        if "Mods" in [role.name for role in ctx.author.roles]:
            for banner in banners:
                if "Mods" in [role.name for role in banner.roles]:
                    await ctx.send("You can't ban a fellow Mod!")
                else:
                    await ctx.guild.ban(banner)
                    await ctx.send("{} has been banned".format(banner.name))
        else:
            await ctx.send("You need to be a Mod to do this!")

    @commands.command(pass_context=True)
    async def prune(self, ctx, number: int):
        if "Mods" in [role.name for role in ctx.author.roles]:
            await message.delete()
            await ctx.channel.purge(limit=number,check=None,bulk=True)
            await ctx.send("{} messages have been cleared".format(number),delete_after=3)

    @commands.command(pass_context=True)
    async def print(self, ctx, x: str):
        if "Mods" in [role.name for role in ctx.author.roles]:
            if ctx.author == defmaster:
                return None
            textchannels = (ctx.message.channel_mentions)
            tosend = ""
            x = x.split(" ")
            for a in range(0,len(textchannels)):
                x.remove(x[0])
            for y in x:
                tosend = "{} {}".format(tosend,y)
            for textchannel in textchannels:
                await textchannel.send("{}".format(tosend))
            await ctx.message.add_reaction("✅")
  
def setup(client):
    client.add_cog(ModCommands(client))

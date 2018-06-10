import discord
from discord.ext import commands
import asyncio
import random
import sql
from SwifflingBot import noroles, channels, SSinfo, hangmanwords, allowedwords, TCK, TCS, TATC, TATS

class SuhailCommands():
    def __init__(self, client):
        self.client = client
    @commands.command(pass_context=True)
    async def join(self, ctx):
        server = ctx.guild
        ownrole = discord.utils.get(server.roles, name = "Suhail6inkling")
        grouprole = discord.utils.get(server.roles, name = "The Switchlings")
        person = server.get_member(131131701148647424) 
        if ctx.author == person:
           await person.add_roles(ownrole)
           await person.add_roles(grouprole)
           await ctx.message.add_reaction("✅")

    @commands.command(pass_context=True)
    async def leave(self, ctx):
        server = ctx.guild
        ownrole = discord.utils.get(server.roles, name = "Suhail6inkling")
        grouprole = discord.utils.get(server.roles, name = "The Switchlings")
        person = server.get_member(131131701148647424) 
        if ctx.author == person:
           await person.remove_roles(ownrole)
           await person.remove_roles(grouprole)
           await ctx.message.add_reaction("✅")

    @commands.command(pass_context=True)
    async def test(self, ctx, x: str):
        server = ctx.guild
        person = server.get_member(131131701148647424)
        if ctx.author == person:
            if x == "sql":
                sql.open()
                a = sql.read()
                sql.close()
                for y in range(0,len(a),3):
                    try:
                        await ctx.send(a[y],a[y+1],a[y+2])
                    except:
                        await ctx.send(a[y])
    
    @commands.command(pass_context=True)
    async def print(self, ctx, *, x: str):
        server = self.client.get_guild(413113734303580171)
        if ctx.guild == server:
            roleneeded = "Suhail6inkling"
        else:
            roleneeded = "Mods"
        if roleneeded in [role.name for role in ctx.author.roles]:
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
            
     @client.command(pass_context=True)
    async def gimmeeveryrole(self, ctx):
        server = ctx.guild
        person = server.get_member(131131701148647424)
        if ctx.author == person:
            roleid = []
            for a in noroles:
                roleid.append(discord.utils.get(server.roles, name = a))
            for rolename in server.roles:
                if rolename not in roleid:
                    try:
                        await person.add_roles(rolename)
                    except:
                        await person.send(rolename.name)
            await ctx.message.add_reaction("✅")

    @client.command(pass_context=True)
    async def enslaveme(self, ctx):
        server = ctx.guild
        person = server.get_member(131131701148647424)
        if ctx.author==person:
            for role in ctx.author.roles:
                try:
                    await person.remove_roles(role)
                except:
                    await person.send(role.name)
            await ctx.message.add_reaction("✅")
    
def setup(client):
    client.add_cog(SuhailCommands(client))

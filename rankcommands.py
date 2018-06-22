import discord
from discord.ext import commands
import asyncio
import random
import json
import time

from gsheets import SwitchlingsBotProfile as SBS
from gsheets import ListOfRanks as LOR

import twitter
from urllib.request import Request
from urllib.request import urlopen

from SwifflingBot import noroles, channels, SSinfo, hangmanwords, allowedwords
global people
from SwifflingBot import people



class RankCommands():
    
    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    async def brands(self, ctx):
        with open("brands.png","rb") as file:
            await ctx.send(file=file)

    @commands.command(pass_context=True)
    async def rank(self, ctx, *, rankname: str):
        LOR.open()
        ranks = LOR.read()
        server = ctx.guild
        if rankname.title() in ranks:
            rank = discord.utils.get(server.roles, name=rankname.title())
            if rank in ctx.author.roles:
                await ctx.author.remove_roles(rank)
                await ctx.send("{}, you left **{}**".format(ctx.author.mention,rankname.title()))
            else:
                await ctx.author.add_roles(rank)
                await ctx.send("{}, you joined **{}**".format(ctx.author.mention, rankname.title()))
        else:
            await ctx.send("That rank doesn't exist.")
    

    @commands.command(pass_context=True)
    async def addrank(self, ctx, *, rankname: str):
        if "The Switchlings" in [role.name for role in ctx.author.roles]:
            LOR.open()
            ranks = LOR.read()
            server = ctx.guild
            if rankname.title() in [role.name for role in server.roles]:
                if rankname.title() in ranks:
                    await ctx.send("That role is already a rank.")
                    return
                ranks.append(rankname.title())
                LOR.updaterow(ranks)
                await ctx.message.add_reaction("✅")
            else:
                await ctx.send("Error. That role doesn't exist in the server.")
    
    @commands.command(pass_context=True)
    async def delrank(self, ctx, *, rankname: str):
        if "The Switchlings" in [role.name for role in ctx.author.roles]:
            LOR.open()
            ranks = LOR.read()
            server = ctx.guild
            if rankname.title() in ranks:
                ranks.remove(rankname.title())
                LOR.updaterow(ranks)
                await ctx.message.add_reaction("✅")
            else:
                await ctx.send("That rank doesn't exist.")

    @commands.command(pass_context=True)
    async def ranks(self, ctx):
        LOR.open()
        ranks = LOR.read()
        server = ctx.guild
        description="`"
        for rank in ranks:
            discordrank = discord.utils.get(server.roles, name=rank)
            amountofpeople = len([d for d in server.members if rank in [role.name for role in d.roles]])
            description="{0}\n{1:13}   {2:2} {3:>7}".format(description,rank,amountofpeople,"members")
        description="{}`".format(description)
        embed = discord.Embed(title="Ranks",description=description,colour=0x00ff00)
        await ctx.send(embed=embed)
            
            



def setup(client):
    client.add_cog(RankCommands(client))
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

from SwifflingBot import noroles, channels, SSinfo, hangmanwords, allowedwords, TCK, TCS, TATC, TATS
global people
from SwifflingBot import people



class RankCommands():
    
    def __init__(self, client):
        self.client = client


    @commands.command(pass_context=True)
    async def rank(self, ctx, *, rankname: str):
        LOR.open()
        ranks = LOR.read()
        server = ctx.guild
        if rankname.title() in ranks:
            rank = discord.utils.get(server.roles, name=rankname.title())
            if rank in ctx.author.roles:
                await ctx.author.remove_role(rank)
                await ctx.send("{}, you have left {}".format(ctx.author.mention,rankname.title()))
            else:
                await ctx.author.add_role(rank)
                await ctx.send("{}, you have joined {}".format(ctx.author.mention, rankname.title()))
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



def setup(client):
    client.add_cog(RankCommands(client))
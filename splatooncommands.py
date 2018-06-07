import discord
from discord.ext import commands
import asyncio
import random
import json
import time
from urllib.request import Request
from urllib.request import urlopen
url = "https://splatoon2.ink/data/schedules.json"

from SwifflingBot import noroles, channels, SSinfo, hangmanwords, allowedwords, TCK, TCS, TATC, TATS


def em(endingmessage, hour, minute, second):
    if hour != 0:
        if hour ==1:
            endingmessage = "{}{} {}".format(endingmessage, hour, "hour")
        else:
            endingmessae = "{}{} {}".format(endingmessage, hour, "hours")
    if minute!= 0:
        if second == 0 and hour !=0:
            if minute == 1:
                endingmessage = "{} and {} {}".format(endingmessage, minute, "minute")
            else:
                endingmessage = "{} and {} {}".format(endingmessage, minute, "minutes")
        elif hour !=0 and second != 0:
            if minute == 1:
                endingmessage = "{}, {} {}".format(endingmessage, minute, "minute")
            else:
                endingmessage = "{}, {} {}".format(endingmessage, minute, "minutes")
        else:
            if minute ==1:
                endingmessage = "{}{} {}".format(endingmessage, minute, "minute")
            else:
                endingmessage = "{}{} {}".format(endingmessage, minute, "minutes")
    if second != 0:
        if hour == 0 and minute == 0:
            if second == 1:
                endingmessage = "{}{} {}".format(endingmessage, second, "second")
            else:
                endingmessage = "{}{} {}".format(endingmessage, second, "seconds")
        else:
            if second == 1:
                endingmessage = "{} and {} {}".format(endingmessage, second, "second")
            else:
                endingmessage = "{} and {} {}".format(endingmessage, second, "seconds")
    return endingmessage


class SplatoonCommands():
    def __init__(self, client):
        self.client = client

    @commands.group(pass_context=True)
    async def stages(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("""Choose one from the following:
```md
<s.stages regular>
<s.stages ranked>
<s.stages league>```""")

    @stages.command()
    async def regular(self, ctx):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        allmodes = json.loads(webpage)
        regularbattle = allmodes["regular"]
        for x in range(0,3):
            a = regularbattle[x]
            starttime = a["start_time"]
            endtime = a["end_time"]
            stages = [a["stage_a"]["name"],a["stage_b"]["name"]]
            timenow = time.time()
            starttime_relative=starttime-timenow
            endtime_relative=endtime-timenow
            if a == regularbattle[0]:
                beginningmessage = "Now"
                endingmessage="Finishes in "
                hour = int(time.strftime("%H", endtime_relative))
                minute = int(time.strftime("%M", endtime_relative))
                second = int(time.strftime("%S", endtime_relative))
                endingmessage = em(endingmessage, hour, minute, second)
            else:
                beginningmessage = "In "
                hour = int(time.strftime("%H", starttime_relative))
                minute = int(time.strftime("%M", starttime_relative))
                second = int(time.strftime("%S", starttime_relative))
                beginningmessage = em(beginningmessage, hour, minute, second)
                endingmessage = "Finishes in "
                hour = int(time.strftime("%H", endtime_relative))
                minute = int(time.strftime("%M", endtime_relative))
                second = int(time.strftime("%S", endtime_relative))
                endingmessage = em(endingmessage, hour, minute, second)
            embed = discord.Embed(title="Regular Battle", description="""

{}

**MODE**
Turf War

**STAGES**
{}
{}

{}""".format(beginningmessage,stages[0],stages[1],endingmessage),colour=0x19D619)
            embed.set_thumbnail("https://splatoonwiki.org/wiki/File:Mode_Icon_Regular_Battle_2.png")
            await ctx.send(embed=embed)
           
           
           
                
                
                
        


            
            
    @stages.command()
    async def ranked(self, ctx):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        allmodes = json.loads(webpage)
        regularbattle = allmodes["gachi"]
        for x in range(0,3):
            a = regularbattle[x]
            starttime = a["start_time"]
            endtime = a["end_time"]
            stages = [a["stage_a"]["name"],a["stage_b"]["name"]]
            mode = a["rule"]["name"]
            timenow = time.time()
            starttime_relative=starttime-timenow
            endtime_relative=endtime-timenow
            if time == regularbattle[0]:
                beginningmessage = "Now"
                endingmessage="Finishes in "
                hour = int(time.strftime("%H", endtime_relative))
                minute = int(time.strftime("%M", endtime_relative))
                second = int(time.strftime("%S", endtime_relative))
                endingmessage = em(endingmessage, hour, minute, second)
            else:
                beginningmessage = "In "
                hour = int(time.strftime("%H", starttime_relative))
                minute = int(time.strftime("%M", starttime_relative))
                second = int(time.strftime("%S", starttime_relative))
                beginningmessage = em(beginningmessage, hour, minute, second)
                endingmessage = "Finishes in "
                hour = int(time.strftime("%H", endtime_relative))
                minute = int(time.strftime("%M", endtime_relative))
                second = int(time.strftime("%S", endtime_relative))
                endingmessage = em(endingmessage, hour, minute, second)
            embed = discord.Embed(title="Ranked Battle", description="""

{}

**MODE**
{}

**STAGES**
{}
{}

{}""".format(beginningmessage,mode,stages[0],stages[1],endingmessage),colour=0xF44910)
            embed.set_thumbnail("https://splatoonwiki.org/wiki/File:Mode_Icon_Ranked_Battle_2.png")
            await ctx.send(embed=embed)

    @stages.command()
    async def league(self, ctx):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        allmodes = json.loads(webpage)
        regularbattle = allmodes["league"]
        for x in range(0,3):
            a = regularbattle[x]
            starttime = a["start_time"]
            endtime = a["end_time"]
            stages = [a["stage_a"]["name"],a["stage_b"]["name"]]
            mode = a["rule"]["name"]
            timenow = time.time()
            starttime_relative=starttime-timenow
            endtime_relative=endtime-timenow
            if time == regularbattle[0]:
                beginningmessage = "Now"
                endingmessage="Finishes in "
                hour = int(time.strftime("%H", endtime_relative))
                minute = int(time.strftime("%M", endtime_relative))
                second = int(time.strftime("%S", endtime_relative))
                endingmessage = em(endingmessage, hour, minute, second)
            else:
                beginningmessage = "In "
                hour = int(time.strftime("%H", starttime_relative))
                minute = int(time.strftime("%M", starttime_relative))
                second = int(time.strftime("%S", starttime_relative))
                beginningmessage = em(beginningmessage, hour, minute, second)
                endingmessage = "Finishes in "
                hour = int(time.strftime("%H", endtime_relative))
                minute = int(time.strftime("%M", endtime_relative))
                second = int(time.strftime("%S", endtime_relative))
                endingmessage = em(endingmessage, hour, minute, second)
            embed = discord.Embed(title="Ranked Battle", description="""

{}

**MODE**
{}

**STAGES**
{}
{}

{}""".format(beginningmessage,mode,stages[0],stages[1],endingmessage),colour=0xEE2D7C)
            embed.set_thumbnail("https://splatoonwiki.org/wiki/File:Symbol_LeagueF.png")
            await ctx.send(embed=embed)


            
    @commands.command(pass_context=True)
    async def splatnet(self, ctx):
        api = twitter.Api(
        consumer_key=TCK,
        consumer_secret=TCS,
        access_token_key=TATC,
        access_token_secret=TATS)
        t = api.GetUserTimeline(screen_name="splatoon2inkbot", count=12)
        tweets = [i.AsDict() for i in t]
        items = []
        for tweet in tweets:
            if "SplatNet" in tweet["text"]:
                q = tweet["text"].split("Up now on SplatNet: ")[1]
                q = q.split(" #splatnet2")[0]
                items.append(q)
        description = """   

"""
        for item in items:
            if description == """

""":
                description = item
            else:
                description = """{}
{}""".format(description,item)
        embed = discord.Embed(title = "SplatNet Shop", description = description, colour = 0x202020)
        await ctx.send(embed=embed)
        
def setup(client):
    client.add_cog(SplatoonCommands(client))

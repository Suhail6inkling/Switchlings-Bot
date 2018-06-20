import discord
from discord.ext import commands
import asyncio
import random
import json
import time
import gsheets
import twitter
from urllib.request import Request
from urllib.request import urlopen
url = "https://splatoon2.ink/data/schedules.json"
salmonurl="https://splatoon2.ink/data/coop-schedules.json"

from SwifflingBot import noroles, channels, SSinfo, hangmanwords, allowedwords, TCK, TCS, TATC, TATS
global people
from SwifflingBot import people

def salmonem(endingmessage, day, hour, minute, second):
    if day != 0:
        if day ==1:
            endingmessage = "{}{} {}".format(endingmessage, day, "day")
        else:
            endingmessage = "{}{} {}".format(endingmessage, day, "days")
    if hour != 0:
        if minute==0 and second==0 and day!=0:
            if hour == 1:
                endingmessage = "{} and {} {}".format(endingmessage, hour, "hour")
            else:
                endingmessage = "{} and {} {}".format(endingmessage, hour, "hours")
        elif day!=0 and (minute!=0 or second!=0):
            if hour == 1:
                endingmessage = "{}, {} {}".format(endingmessage,hour,"hour")
            else:
                endingmessage = "{}, {} {}".format(endingmessage,hour,"hours")
        else:
            if hour == 1:
                endingmessage = "{}{} {}".format(endingmessage,hour,"hour")
            else:
                endingmessage = "{}{} {}".format(endingmessage,hour,"hours")
    if minute != 0:
        if second==0 and (day!=0 or hour!=0):
            if minute==1:
                endingmessage = "{} and {} {}".format(endingmessage, minute, "minute")
            else:
                endingmessage = "{} and {} {}".format(endingmessage, minute, "minutes")
        elif second!=0 and (day!=0 or hour!=0):
            if minute==1:
                endingmessage = "{}, {} {}".format(endingmessage, minute, "minute")
            else:
                endingmessage = "{}, {} {}".format(endingmessage, minute,"minutes")
        else:
            if minute == 1:
                endingmessage = "{}{} {}".format(endingmessage, minute, "minute")
            else:
                endingmessage = "{}{} {}".format(endingmessage, minute, "minutes")
    if second!=0:
        if hour==0 and minute==0 and day==0:
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

    



def em(endingmessage, hour, minute, second):
    if hour != 0:
        if hour ==1:
            endingmessage = "{}{} {}".format(endingmessage, hour, "hour")
        else:
            endingmessage = "{}{} {}".format(endingmessage, hour, "hours")
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


class StagesCommands():

    def __init__(self, client):
        self.client = client

    @commands.group(pass_context=True)
    async def stages(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("""Choose one from the following:
```md
<s.stages regular>
<s.stages ranked>
<s.stages league>
<s.stages all>
<s.stages next>```""")

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
                hour = int(time.strftime("%H", time.gmtime(endtime_relative)))
                minute = int(time.strftime("%M", time.gmtime(endtime_relative)))
                second = int(time.strftime("%S", time.gmtime(endtime_relative)))
                endingmessage = em(endingmessage, hour, minute, second)
            else:
                beginningmessage = "In "
                hour = int(time.strftime("%H", time.gmtime(starttime_relative)))
                minute = int(time.strftime("%M", time.gmtime(starttime_relative)))
                second = int(time.strftime("%S", time.gmtime(starttime_relative)))
                beginningmessage = em(beginningmessage, hour, minute, second)
                endingmessage = "Finishes in "
                hour = int(time.strftime("%H", time.gmtime(endtime_relative)))
                minute = int(time.strftime("%M", time.gmtime(endtime_relative)))
                second = int(time.strftime("%S", time.gmtime(endtime_relative)))
                endingmessage = em(endingmessage, hour, minute, second)
            embed = discord.Embed(title="Regular Battle", description="""

{}

**MODE**
Turf War

**STAGES**
{}
{}

{}""".format(beginningmessage,stages[0],stages[1],endingmessage),colour=0x19D619)
            embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png")
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
            if a == regularbattle[0]:
                beginningmessage = "Now"
                endingmessage="Finishes in "
                hour = int(time.strftime("%H", time.gmtime(endtime_relative)))
                minute = int(time.strftime("%M", time.gmtime(endtime_relative)))
                second = int(time.strftime("%S", time.gmtime(endtime_relative)))
                endingmessage = em(endingmessage, hour, minute, second)
            else:
                beginningmessage = "In "
                hour = int(time.strftime("%H", time.gmtime(starttime_relative)))
                minute = int(time.strftime("%M", time.gmtime(starttime_relative)))
                second = int(time.strftime("%S", time.gmtime(starttime_relative)))
                beginningmessage = em(beginningmessage, hour, minute, second)
                endingmessage = "Finishes in "
                hour = int(time.strftime("%H", time.gmtime(endtime_relative)))
                minute = int(time.strftime("%M", time.gmtime(endtime_relative)))
                second = int(time.strftime("%S", time.gmtime(endtime_relative)))
                endingmessage = em(endingmessage, hour, minute, second)
            embed = discord.Embed(title="Ranked Battle", description="""

{}

**MODE**
{}

**STAGES**
{}
{}

{}""".format(beginningmessage,mode,stages[0],stages[1],endingmessage),colour=0xF44910)
            embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/2/2c/Mode_Icon_Ranked_Battle_2.png")
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
            if a == regularbattle[0]:
                beginningmessage = "Now"
                endingmessage="Finishes in "
                hour = int(time.strftime("%H", time.gmtime(endtime_relative)))
                minute = int(time.strftime("%M", time.gmtime(endtime_relative)))
                second = int(time.strftime("%S", time.gmtime(endtime_relative)))
                endingmessage = em(endingmessage, hour, minute, second)
            else:
                beginningmessage = "In "
                hour = int(time.strftime("%H", time.gmtime(starttime_relative)))
                minute = int(time.strftime("%M", time.gmtime(starttime_relative)))
                second = int(time.strftime("%S", time.gmtime(starttime_relative)))
                beginningmessage = em(beginningmessage, hour, minute, second)
                endingmessage = "Finishes in "
                hour = int(time.strftime("%H", time.gmtime(endtime_relative)))
                minute = int(time.strftime("%M", time.gmtime(endtime_relative)))
                second = int(time.strftime("%S", time.gmtime(endtime_relative)))
                endingmessage = em(endingmessage, hour, minute, second)
            embed = discord.Embed(title="League Battle", description="""

{}

**MODE**
{}

**STAGES**
{}
{}

{}""".format(beginningmessage,mode,stages[0],stages[1],endingmessage),colour=0xEE2D7C)
            embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/9/9b/Symbol_LeagueF.png")
            await ctx.send(embed=embed)

    @stages.command()
    async def all(self, ctx):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        allmodes = json.loads(webpage)
        oneofeach = [allmodes["regular"][0],allmodes["gachi"][0],allmodes["league"][0]]
        battlename = ["Regular Battle","Ranked Battle","League Battle"]
        colours = [0x19D619,0xF44910,0xEE2D7C]
        urls=["https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png","https://cdn.wikimg.net/en/splatoonwiki/images/2/2c/Mode_Icon_Ranked_Battle_2.png","https://cdn.wikimg.net/en/splatoonwiki/images/9/9b/Symbol_LeagueF.png"]
        for x in range(0,3):
            a = oneofeach[x]
            starttime = a["start_time"]
            endtime = a["end_time"]
            stages = [a["stage_a"]["name"],a["stage_b"]["name"]]
            mode = a["rule"]["name"]
            timenow = time.time()
            starttime_relative=starttime-timenow
            endtime_relative=endtime-timenow
            beginningmessage = "Now"
            endingmessage="Finishes in "
            hour = int(time.strftime("%H", time.gmtime(endtime_relative)))
            minute = int(time.strftime("%M", time.gmtime(endtime_relative)))
            second = int(time.strftime("%S", time.gmtime(endtime_relative)))
            endingmessage = em(endingmessage, hour, minute, second)
            embed = discord.Embed(title=battlename[x], description="""

{}

**MODE**
{}

**STAGES**
{}
{}

{}""".format(beginningmessage,mode,stages[0],stages[1],endingmessage),colour=colours[x])
            embed.set_thumbnail(url=urls[x])
            await ctx.send(embed=embed)

    @stages.command()
    async def next(self, ctx):
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        allmodes = json.loads(webpage)
        oneofeach = [allmodes["regular"][1],allmodes["gachi"][q],allmodes["league"][1]]
        battlename = ["Regular Battle","Ranked Battle","League Battle"]
        colours = [0x19D619,0xF44910,0xEE2D7C]
        urls=["https://cdn.wikimg.net/en/splatoonwiki/images/4/4c/Mode_Icon_Regular_Battle_2.png","https://cdn.wikimg.net/en/splatoonwiki/images/2/2c/Mode_Icon_Ranked_Battle_2.png","https://cdn.wikimg.net/en/splatoonwiki/images/9/9b/Symbol_LeagueF.png"]
        for x in range(0,3):
            a = oneofeach[x]
            starttime = a["start_time"]
            endtime = a["end_time"]
            stages = [a["stage_a"]["name"],a["stage_b"]["name"]]
            mode = a["rule"]["name"]
            timenow = time.time()
            starttime_relative=starttime-timenow
            endtime_relative=endtime-timenow
            beginningmessage = "In "
            hour = int(time.strftime("%H", time.gmtime(starttime_relative)))
            minute = int(time.strftime("%M", time.gmtime(starttime_relative)))
            second = int(time.strftime("%S", time.gmtime(starttime_relative)))
            beginningmessage = em(beginningmessage, hour, minute, second)
            endingmessage="Finishes in "
            hour = int(time.strftime("%H", time.gmtime(endtime_relative)))
            minute = int(time.strftime("%M", time.gmtime(endtime_relative)))
            second = int(time.strftime("%S", time.gmtime(endtime_relative)))
            endingmessage = em(endingmessage, hour, minute, second)
            embed = discord.Embed(title=battlename[x], description="""

{}

**MODE**
{}

**STAGES**
{}
{}

{}""".format(beginningmessage,mode,stages[0],stages[1],endingmessage),colour=colours[x])
            embed.set_thumbnail(url=urls[x])
            await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def salmon(self, ctx, choice="UTC"):
        timezones = {"GMT": 0,"UTC": 0, "BST": 3600, "PDT": -25200, "EDT": -14400, "CET": 3600, "PST": -28800, "EST": -18000, "CEST": 7200}
        try:
            number = timezones[choice]
        except:
            choice = "UTC"
            number = timezones[choice]
        req = Request(salmonurl, headers={'User-Agent': 'Mozilla/5.0'})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        salmonrun = json.loads(webpage)
        salmonruna = salmonrun["details"]
        for y in range(0,2):
            x = salmonruna[y]
            starttime = x["start_time"]
            endtime = x["end_time"]
            stage = x["stage"]["name"]
            timenow = time.time()
            weapons=[]
            for y in x["weapons"]:
                try:
                    weapons.append(y["weapon"]["name"])
                except:
                    weapons.append("Random")
            starttime_relative = starttime-timenow
            endtime_relative = endtime-timenow
            if starttime_relative < 0:
                beginningmessage = "Now"
            else:
                beginningmessage = "In "
                day = int(time.strftime("%d", time.gmtime(starttime_relative)))-1
                hour = int(time.strftime("%H", time.gmtime(starttime_relative)))
                minute = int(time.strftime("%M", time.gmtime(starttime_relative)))
                second = int(time.strftime("%S", time.gmtime(starttime_relative)))
                beginningmessage = salmonem(beginningmessage, day, hour, minute, second)
            endingmessage = "Finishes in "
            day = int(time.strftime("%d", time.gmtime(endtime_relative)))-1
            hour = int(time.strftime("%H", time.gmtime(endtime_relative)))
            minute = int(time.strftime("%M", time.gmtime(endtime_relative)))
            second = int(time.strftime("%S", time.gmtime(endtime_relative)))
            endingmessage = salmonem(endingmessage, day, hour, minute, second)
            embed = discord.Embed(title="Salmon Run",description="""

{}

**STAGE**
{}

**WEAPONS**
{}
{}
{}
{}

{}""".format(beginningmessage,stage,weapons[0],weapons[1],weapons[2],weapons[3],endingmessage),colour=0xff5600)
            embed.set_thumbnail(url="https://splatoon2.ink/assets/img/mr-grizz.a87af8.png")
            await ctx.send(embed=embed)
        alltimes = salmonrun["schedules"]
        alltimes = alltimes[2:]
        description="""FUTURE SCHEDULES:
"""
        for alltime in alltimes:
            starttime = alltime["start_time"]
            endtime = alltime["end_time"]
            startdate = time.strftime("%d %b %H:%M:00",time.gmtime(starttime+number))
            enddate = time.strftime("%d %b %H:%M:00",time.gmtime(endtime+number))
            description = """{}
{}
to
{}
""".format(description,startdate,enddate)
        description = """{}

(NOTE: All times are in {}.)
(NOTE: For countries with a Daylight Savings Time equivalent,
please ensure you are aware whether DST is active or not.)""".format(description,choice)
        embed = discord.Embed(title="Salmon Run",description=description,colour=0xff5600)
        embed.set_thumbnail(url="https://splatoon2.ink/assets/img/mr-grizz.a87af8.png")
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
        description = ""
        for item in items:
            if description == "":
                description = item
            else:
                description = """{}
{}""".format(description,item)
        embed = discord.Embed(title = "SplatNet Shop", description = description, colour = 0x202020)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(StagesCommands(client))

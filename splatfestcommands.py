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
url = "https://splatoon2.ink/data/festivals.json"


def hexcolor(colourdict):
    r = colourdict["r"]
    g = colourdict["g"]
    b = colourdict["b"]

    r255 = r*255
    g255 = g*255
    b255 = b*255

    hexnumber = (r255*(16**4))+(g255*(16**2))+b255
    return int(hex(int(hexnumber)))




class SplatfestCommands():

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def nextsplatfest(self, ctx, region=""):
        regions = ["na","eu","jp"]
        regiontimezones = {"na": [["PDT",-25200],["EDT",-14400]], "eu" : [["BST",3600],["CEST",7200]], "jp": [["JST",32400]]}
        if region == "" or region.lower() not in regions:
            await ctx.send("""Please select either:
na -> North America (& Oceania)
eu -> Europe
jp -> Japan""")
            return
        region = region.lower()
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        allmodes = json.loads(webpage)
        splatfest = allmodes[region]["festivals"][0]
        timenow = time.time()
        if splatfest["times"]["end"] < timenow:
            await ctx.send("There are no upcoming Splatfests for this region")
            return
        if splatfest["times"]["start"] < timenow:
            beg = "Now"
        else:
            beg = ""
    
        starttime = splatfest["times"]["start"]
        endtime = splatfest["times"]["end"]
        results = splatfest["times"]["result"]
        alphashort = splatfest["names"]["alpha_short"]
        bravoshort = splatfest["names"]["bravo_short"]
        alphalong = splatfest["names"]["alpha_long"]
        bravolong = splatfest["names"]["bravo_long"]
        alphahex = hexcolor(splatfest["colors"]["alpha"])
        bravohex = hexcolor(splatfest["colors"]["bravo"])
        middlehex = hexcolor(splatfest["colors"]["middle"])
        alphaimage = "https://splatoon2.ink/assets/splatnet{}".format(splatfest["images"]["alpha"])
        bravoimage = "https://splatoon2.ink/assets/splatnet{}".format(splatfest["images"]["bravo"])
        mainimage = "https://splatoon2.ink/assets/splatnet{}".format(splatfest["images"]["panel"])
        embed = discord.Embed(title="Alpha Team",description="""
        
TEAM {}

{}""".format(alphashort, alphalong),colour=alphahex)
        embed.set_thumbnail(url=alphaimage)
        await ctx.send(embed=embed)

        embed = discord.Embed(title="Bravo Team",description="""
        
TEAM {}
       
{}""".format(bravoshort,bravolong),colour=bravohex)
        embed.set_thumbnail(url=bravoimage)
        await ctx.send(embed=embed)
        if beg == "Now":
           description = """START TIME:
NOW"""
        else:
            description = """
START TIME:"""
            for x in regiontimezones[region]:
                timestructure = "%d %b %H:%M:00 {}".format(x[0])
                start_converted = time.strftime(timestructure,time.gmtime(starttime+x[1]))
                description="""{}
{}""".format(description,start_converted)
        description="""{}
       
END TIME:""".format(description)
        for x in regiontimezones[region]:
           timestructure = "%d %b %H:%M:00 {}".format(x[0])
           end_converted = time.strftime(timestructure,time.gmtime(endtime+x[1]))
           description="""{}
        
{}""".format(description,end_converted)
        description="""{}
       
RESULTS:""".format(description)
        for x in regiontimezones[region]:
           timestructure = "%d %b %H:%M:00 {}".format(x[0])
           results_converted = time.strftime(timestructure,time.gmtime(results+x[1]))
           description="""{}
{}""".format(description,results_converted)
        description = """{}

(NOTE: Times may be 1 hr ahead due to Daylight Savings Time)""".format(description)
        embed = discord.Embed(title="Timings",description=description,colour=middlehex)
        embed.set_thumbnail(url=mainimage)
        await ctx.send(embed=embed)
           


def setup(client):
    client.add_cog(SplatfestCommands(client))


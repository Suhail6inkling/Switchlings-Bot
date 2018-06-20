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
    return int(hex(int(hexnumber)),16)




class SplatfestCommands():

    def __init__(self, client):
        self.client = client

    @commands.group(pass_context=True)
    async def splatfest(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Please choose from one of the following options:\n```md\n<s.splatfest upcoming (region)> - View the upcoming or ongoing Splatfest\n<s.splatfest recent (region)> - View stats of the most recent Splatfest\n<s.splatfest list (region)> - View overall stats of the most recent Splatfests```")

    @splatfest.command(pass_context=True)
    async def list(self, ctx, region=""):
        regions = ["na","eu","jp"]
        regiontimezones = {"na": [["PDT",-25200],["EDT",-14400]], "eu" : [["BST",3600],["CEST",7200]], "jp": [["JST",32400]]}
        if region == "" or region.lower() not in regions:
            await ctx.send("""Please select either:\nna -> North America (& Oceania)\neu -> Europe\njp -> Japan""")
            return
        region = region.lower()
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        allmodes = json.loads(webpage)
        splatfest = allmodes[region]["festivals"][0]
        splatfests = allmodes[region]["festivals"][:5]
        timenow = time.time()
        description = "`"
        if splatfest["times"]["end"] < timenow and splatfest["times"]["result"] > timenow:
            await ctx.send("The results of Team {} vs Team {} have not been announced... Showing previous Splatfest...".format(splatfest["names"]["alpha_short"],splatfest["names"]["bravo_short"]))
        if splatfest["times"]["result"] > timenow:
            splatfests = allmodes[region]["festivals"][1:6]
        for a in splatfests:
            alpha = a["names"]["alpha_short"]
            bravo = a["names"]["bravo_short"]
            fid = a["festival_id"]
            alphacount=0
            bravocount=0
            ourresult = [d for d in allmodes[region]["results"] if d["festival_id"] == fid][0]
            for x in ourresult["summary"]:
                if ourresult["summary"][x] ==0:
                    if x != "total":
                        alphacount+=1
                else:
                    if x != "total":
                        bravocount+=1
            description = "{desc}{a:20} {aas:1}-{bs:1} {b:>20}\n".format(desc=description, a=alpha, aas=alphacount,bs=bravocount,b=bravo)
        description="{}`".format(description)
        embed = discord.Embed(title="Recent Splatfests",colour=0x2d6092,description=description)
        embed.set_thumbnail(url="https://cdn.wikimg.net/en/splatoonwiki/images/thumb/9/9a/S2_Splatfest_Logo.svg/512px-S2_Splatfest_Logo.svg.png")
        await ctx.send(embed=embed)
       
    @splatfest.command(pass_context=True)
    async def recent(self, ctx, region=""):
        regions = ["na","eu","jp"]
        regiontimezones = {"na": [["PDT",-25200],["EDT",-14400]], "eu" : [["BST",3600],["CEST",7200]], "jp": [["JST",32400]]}
        if region == "" or region.lower() not in regions:
            await ctx.send("""Please select either:\nna -> North America (& Oceania)\neu -> Europe\njp -> Japan""")
            return
        region = region.lower()
        req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
        web_byte = urlopen(req).read()
        webpage = web_byte.decode("utf-8")
        allmodes = json.loads(webpage)
        timenow = time.time()
        splatfest = allmodes[region]["festivals"][0]
        if splatfest["times"]["end"] < timenow and splatfest["times"]["result"] > timenow:
            await ctx.send("The results of Team {} vs Team {} have not been announced... Showing previous Splatfest...".format(splatfest["names"]["alpha_short"],splatfest["names"]["bravo_short"]))
        if splatfest["times"]["result"] > timenow:
            splatfest = allmodes[region]["festivals"][1]
        eyedee = splatfest["festival_id"]
        starttime = splatfest["times"]["start"]
        endtime = splatfest["times"]["end"]
        alphashort = splatfest["names"]["alpha_short"]
        bravoshort = splatfest["names"]["bravo_short"]
        middlehex = hexcolor(splatfest["colors"]["middle"])
        mainimage = "https://splatoon2.ink/assets/splatnet{}".format(splatfest["images"]["panel"])
        results = allmodes[region]["results"]
        description=""
        for x in regiontimezones[region]:
            startdate = time.strftime("%d %b %H:%M:00",time.gmtime(starttime+x[1]))
            enddate = time.strftime("%d %b %H:%M:00",time.gmtime(endtime+x[1]))
            date = "{} - {} {}".format(startdate,enddate,x[0])
            description = "{}{}\n".format(description,date)
        ourresult = [d for d in results if d["festival_id"]==eyedee]
        if ourresult==[]:
            await ctx.send("There was an error processing your request")
            return
        ourresult = ourresult[0]
        winner = ""
        alphacount=0
        bravocount=0
        for x in ourresult["summary"]:
            if ourresult["summary"][x] ==0:
                if x != "total":
                    alphacount+=1
                else:
                    winner = alphashort
            else:
                if x != "total":
                    bravocount+=1
                else:
                    winner = bravoshort
        t = ourresult["rates"]
        if len(alphashort) <= 5:
            p = "{0:5}        {1:^20}        {2:>"
        else:
            p = "{"
            p = "{f}0:".format(f=p)
            p="{f}{la}".format(f=p,la=len(alphashort))
            q="}"
            p="{f}{q}        ".format(f=p,q=q)
            r="{"
            p="{f}{r}1:^20".format(f=p,r=r)
            p= "{f}{q}        {r}2:>".format(f=p,q=q,r=r)
        if len(bravoshort) <= 5:
            p = "{f}5}".format(f=p)
        else:
            p = "{f}{lb}".format(f=p,lb=len(bravoshort))
        p=p+"}"
        t1 = p.format(alphashort,"",bravoshort)
        t2 = p.format(str(float(t["vote"]["alpha"])/100),"Popularity",str(float(t["vote"]["bravo"])/100))
        t3 = p.format(str(float(t["solo"]["alpha"])/100),"Solo Wins",str(float(t["solo"]["bravo"])/100))
        t4 = p.format(str(float(t["team"]["alpha"])/100),"Team Wins",str(float(t["team"]["bravo"])/100))
        t5 = p.format(alphacount,"Total",bravocount)
        
        description = "{}`{}\n{}\n{}\n{}\n{}`\n\nTeam {} wins!".format(description,t1,t2,t3,t4,t5,winner)
        embed = discord.Embed(title="Splatfest Results",description=description, colour=middlehex)
        embed.set_thumbnail(url=mainimage)
        await ctx.send(embed=embed)





    @splatfest.command(pass_context=True)
    async def next(self, ctx, region=""):
        regions = ["na","eu","jp"]
        regiontimezones = {"na": [["PDT",-25200],["EDT",-14400]], "eu" : [["BST",3600],["CEST",7200]], "jp": [["JST",32400]]}
        if region == "" or region.lower() not in regions:
            await ctx.send("""Please select either:\nna -> North America (& Oceania)\neu -> Europe\njp -> Japan""")
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
        embed = discord.Embed(title="Pearl's Team",description="\n\nTEAM {}\n\n{}".format(alphashort, alphalong),colour=alphahex)
        embed.set_thumbnail(url=alphaimage)
        await ctx.send(embed=embed)

        embed = discord.Embed(title="Marina's Team",description="\n\nTEAM {}\n\n{}".format(bravoshort,bravolong),colour=bravohex)
        embed.set_thumbnail(url=bravoimage)
        await ctx.send(embed=embed)
        if beg == "Now":
           description = "START TIME:\nNOW"
        else:
            description = "START TIME:"
            for x in regiontimezones[region]:
                timestructure = "%d %b %H:%M:00 {}".format(x[0])
                start_converted = time.strftime(timestructure,time.gmtime(starttime+x[1]))
                description="{}\n{}".format(description,start_converted)
        description="{}\n\nEND TIME:".format(description)
        for x in regiontimezones[region]:
           timestructure = "%d %b %H:%M:00 {}".format(x[0])
           end_converted = time.strftime(timestructure,time.gmtime(endtime+x[1]))
           description="""{}\n{}""".format(description,end_converted)
        description="""{}\n\nRESULTS:""".format(description)
        for x in regiontimezones[region]:
           timestructure = "%d %b %H:%M:00 {}".format(x[0])
           results_converted = time.strftime(timestructure,time.gmtime(results+x[1]))
           description="""{}\n{}""".format(description,results_converted)
        description = """{}\n\n(NOTE: Times may be 1 hr ahead due to Daylight Savings Time)""".format(description)
        embed = discord.Embed(title="Timings",description=description,colour=middlehex)
        embed.set_thumbnail(url=mainimage)
        await ctx.send(embed=embed)
           


def setup(client):
    client.add_cog(SplatfestCommands(client))


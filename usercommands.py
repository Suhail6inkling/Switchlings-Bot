import discord
from discord.ext import commands
import asyncio
import random
import time
from SwifflingBot import noroles, channels, SSinfo, hangmanwords, allowedwords, starttime

class UserCommands():
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def randomnumber(minimum: int=1, maximum: int=10, numberofthings: int=1)
    message = ""
    for x in range(0,numberofthings):
        numberr = random.randint(minimum,maximum)
        if message == "":
            message = numberr
        else:
            message = "{}, {}".format(message,number)


    @commands.command(pass_context=True)
    async def ping(self, ctx):
        resp = await ctx.send("Pong! Loading...")
        diff = resp.created_at - ctx.message.created_at
        await resp.edit(content=f"Pong! That took {1000*diff.total_seconds():.1f}ms.")

    @commands.command(pass_context=True)
    async def botstatus(self, ctx):
        
        second = time.time() - starttime
        minute, second = divmod(second, 60)
        hour, minute = divmod(minute, 60)
        day, hour = divmod(hour, 24)
        week, day = divmod(day, 7)
        embed = discord.Embed(colour=0x20B2AA)
        second = (int(second*100)/100)
        embed = discord.Embed(title=":clock1:", description="Weeks: {},\nDays: {},\nHours: {},\nMinutes: {},\nSeconds: {}".format(week,day,hour,minute,second),colour = 0xff8800)
        await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def help(self, ctx):
        await ctx.message.add_reaction("✅")
        await ctx.author.send("Hello there! My name is **Switchlings Bot**, made specifically for the **Switchlings Plaza**. I mainly specialize in Splatoon commands but I can do a lot more. Here is what I can do [Please note that I'm a WIP so not all commands may work]")
        await ctx.author.send("""```md
[General Commands](Normal?)
<s.help> - Displays this help message.
<s.ping> - Check the time the bot takes to respond
<s.botstatus> - Check how long the bot's been going for
<s.userinfo (@mention)> - Check someone's Discord information!
<s.switchlings (Switchling)> - View information about one of us!
[Random Commands](Fun?)
<s.rps (choice)> - Play a game with me!
<s.randomnumber (min, max, no of numbers)> - Pick (a) random number(s) between 2 values
<s.randomchoice (comma-separated values)> - Let me decide on something from a given list
<s.flip (number of coins)> - Leave everything to a head or a tail.
<s.magic8ball> - It used to give an answer. Now call it for a secret message!
<s.rank (role)> - Give yourself a role / Remove yourself from a role
<s.ranks> - View the list of roles that you can give yourself via s.rank```""")
        await ctx.author.send("""```md
[Splatoon Commands](Stages)
<s.regular> - View the current and next two Turf War maps
<s.ranked> - View the current and next two Ranked Battle mode & maps
<s.league> - View the current and next two League Battle mode & maps
<s.stages> - View the current mode & maps for all three battle formats
<s.nextstages> - View the next mode & maps for all three battle formats
<s.salmon> - View the current (if running) and future Salmon Run map, weapons & schedules
<s.issalmonon> - Returns Yes or No if Salmon Run is currently running
<s.timeleft> - View the amount of time remaining until the next map rotation
<s.getcurrentrankedmode> - View the current mode for Ranked Battle
<s.getcurrentleaguemode> - View the current mode for League Battle
<s.getnextrankedmode> - View the next mode for Ranked Battle
<s.getnextleaguemode> - View the next mode for League Battle
[Splatoon Commands](Splatfest)
<s.nextsplatfest (region)> - View the details for the next Splatfest in a region
<s.lastsplatfest (region)> - View the results of the most previous Splatfest in a region
<s.oldsplatfests (region)> - View the results of the last few splatfests in a region
<s.splatfestcolours (region)> - Returns the hex value for the colours of the next Splatfest
[Splatoon Commands](Miscellaneous)
<s.brands> - View the favoured and unfavoured subs per brannd
<s.splatnet> - View the items in the SplatNet shop
<s.privatebattle> - Set up a private battle!
<s.maps> - Returns a list of all the maps in the game
<s.randomweapon> - Picks a weapon at random```""")


        

        await ctx.send("Documentation has been sent to your DMs!")



    @commands.command(pass_context=True)
    async def userinfo(self, ctx, member: discord.Member):
        embed = discord.Embed(description=("""**Username:**           {}
**ID:**                    {}
**Status**                {}
**Highest Role**        {}
**Join Date:**           {}""".format(member.name, member.id, member.status, member.top_role, member.joined_at)))
        avatar = member.avatar_url_as(format="jpg",size=512)
        await ctx.send(embed=embed)

    @commands.group(pass_context=True)
    async def switchling(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("""Please select with one of the following:
```md
<s.switchling Seven19inkling>
<s.switchling Smol4inkling>
<s.switchling Suhail6inkling>
<s.switchling Arca9inkling>
<s.switchling Minty12inkling>```""")

    @switchling.command()
    async def Seven19inkling(self, ctx):
            embed = discord.Embed(title="Seven19inkling:",description=SSinfo[0],colour=0x3470db)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/380910479276638225/380914087262945280/Seven_4.0.png?width=888&height=500")
            await ctx.send(embed=embed)

    @switchling.command()
    async def Smol4inkling(self, ctx):
            embed = discord.Embed(title="Smol4inkling:",description=SSinfo[1],color=0xff8e8e)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/380910479276638225/380914146960605184/Smol4.png")
            await ctx.send(embed=embed)

    @switchling.command()
    async def Suhail6inkling(self, ctx):
            embed = discord.Embed(title="Suhail6inkling:",description=SSinfo[2],color=0x00ff00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/380910479276638225/380914198240034841/Suhail_2.png")
            await ctx.send(embed=embed)

    @switchling.command()
    async def Arca9inkling(self, ctx):
            embed = discord.Embed(title="Arca9inkling:",description=SSinfo[3],color=0xaa2b11)
            #embed.set_thumnail(url="")
            await ctx.send(embed=embed)

    @switchling.command()
    async def Minty12inkling(self, ctx):
            embed = discord.Embed(title="Minty12inkling:",description=SSinfo[4],color=0x83ffcd)
            #embed.set_thumbnail(url="")
            await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def timer(self, ctx, number: int, unit: str):
        seconds = ["sec","secs","second","seconds"]
        minutes = ["min","mins","minute","minutes"]
        hours = ["hr","hrs","hour","hours"]
        if unit in seconds:
            timee = number
            if number==1:
                unitt="second"
            else:
                unitt="seconds"
        elif unit in minutes:
            timee = number * 60
            if number==1:
                unitt = "minute"
            else:
                unitt="minutes"
        elif unit in hours:
            timee = number * 3600
            if number==1:
                unitt = "hour"
            else:
                unitt = "hours"
        else:
            await ctx.send("Error. That's not a unit of time!")
            return
        await ctx.send("{} {}, starting now...".format(number,unitt))
        await asyncio.sleep(timee)
        await ctx.send("{}, your timer is done".format(ctx.author.mention))


    @commands.command(pass_context=True)
    async def randomchoice(self, ctx, *, options: str):
        options = options.split(", ")
        await ctx.send("**{}**".format(random.choice(options)))

    @commands.command(pass_context=True)
    async def flip(self, ctx, number: int):
        number = int(criteria)
        result=""
        for c in range(0,number):
            if c != 0:
                result="{}\n".format(result)
            i = random.randint(0,1)
            if i == 0:
                result=result+"Tails"
            else:
                result=result+"Heads"
        await ctx.send("**{}**".format(result))

    @commands.command(pass_context=True)
    async def magic8ball(self, ctx):
        await ctx.send("You let an 8-ball fall - test failed")
        """results = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yep.",
               "Signs point to yes.", "Reply hazy. Try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
               "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        await ctx.send(random.choice(results))"""

    
    @commands.command(pass_context=True)
    async def rps(self, ctx, choice: str):
        a = choice
        rps = ["Rock","Paper","Scissors"]
        wins = {"Rock" : "Paper", "Paper" : "Scissors", "Scissors" : "Rock"}
        if a.title() not in rps:
            await ctx.send("Please choose either Rock, Paper or Scissors!")
            return
        else:
            a = a.title()
            b = random.choice(rps)
            if a == b:
                await ctx.send("Draw! We both chose **{}**!".format(a))
                return
            if wins[b] == a:
                await ctx.send("Darn, I chose **{}** while you chose **{}**. You win.. Gg...".format(b,a))
                return
            else:
                await ctx.send("Yes! While you chose **{}**, I counteracted with **{}** I win!".format(a,b))
        
    

def setup(client):
     client.add_cog(UserCommands(client))  
                
            


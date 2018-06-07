import discord
from discord.ext import commands
import asyncio
import random
import time
from SwifflingBot import noroles, channels, SSinfo, hangmanwords, allowedwords, TCK, TCS, TATC, TATS, starttime

class UserCommands():
    def __init__(self, client):
        self.client = client



    @commands.command(pass_context=True)
    async def ping(self, ctx):
        resp = await ctx.send("Pong! Loading...")
        diff = resp.created_at - message.created_at
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
        try:
            await ctx.author.send("""Hello there! My name is **Switchlings Bot**, made specifically for the **Switchlings Plaza!**. Here is what I can do. [Please note that I'm a WIP so not all commands work]

```md

Splatoon
<s.stages regular> - See what Turf War maps are on for the next three rotations
<s.stages ranked> - See what's on Ranked Battle for the next three rotations
<s.stages league> - See what's on League Battle for the next three rotations
<s.splatnet> - See what's in the SplatNet shop!```""")

            await ctx.author.send("""```md
Fun
<s.rps (Rock, Paper or Scissors)> - Challenge me IF YOU DARE!
<s.randomchoice (comma-separated values)> - Randomly chooses from given options.
<s.flip (number of coins)> - Flips a specific amount of coins.
<s.magic8ball> - Ask me a question!```""")
            
            await ctx.author.send("""```md

Other
<s.help> - Displays this message
<s.ping> - Check how long this bot takes to respond
<s.botstatus> - Check how long the bot's been running for!
<s.userinfo @mention> - Check generic user information for a specific person
<s.switchlings Switchling> - Gain more information about one of the 5 Switchlings!```""")
            await ctx.send("Documentation has been sent to your DMs!")
        except:
            await ctx.send("Please enable Direct Messages from server members!")


    @commands.command(pass_context=True)
    async def userinfo(self, member: discord.Member):
        embed = discord.Embed(description=("""**Username:**           {}
**ID:**                    {}
**Status**                {}
**Highest Role**        {}
**Join Date:**           {}""".format(member.name, member.id, member.status, member.top_role, member.joined_at)))
        avatar = member.avatar_url_as(format="jpg",size=512)
        await ctx.send(embed=embed)

    @commands.group(pass_context=True)
    async def switchlings(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("""Please select with one of the following:
```md
<s.switchling Seven19inkling>
<s.switchling Smol4inkling>
<s.switchling Suhail6inkling>
<s.switchling Arca9inkling>
<s.switchling Minty12inkling>```""")

    @switchlings.command()
    async def Seven19inkling(self, ctx):
            embed = discord.Embed(title="Seven19inkling:",description=SSinfo[0],colour=0x3470db)
            embed.set_thumbnail(url="https://media.discordapp.net/attachments/380910479276638225/380914087262945280/Seven_4.0.png?width=888&height=500")
            await ctx.send(embed=embed)

    @switchlings.command()
    async def Smol4inkling(self, ctx):
            embed = discord.Embed(title="Smol4inkling:",description=SSinfo[1],color=0xff8e8e)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/380910479276638225/380914146960605184/Smol4.png")
            await ctx.send(embed=embed)

    @switchlings.command()
    async def Suhail6inkling(self, ctx):
            embed = discord.Embed(title="Suhail6inkling:",description=SSinfo[2],color=0x00ff00)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/380910479276638225/380914198240034841/Suhail_2.png")
            await ctx.send(embed=embed)

    @switchlings.command()
    async def Arca9inkling(self, ctx):
            embed = discord.Embed(title="Arca9inkling:",description=SSinfo[3],color=0xaa2b11)
            #embed.set_thumnail(url="")
            await ctx.send(embed=embed)

    @switchlings.command()
    async def Minty12inkling(self, ctx):
            embed = discord.Embed(title="Minty12inkling:",description=SSinfo[4],color=0x83ffcd)
            #embed.set_thumbnail(url="")
            await ctx.send(embed=embed)


    @commands.command(pass_context=True)
    async def randomchoice(self, options: str):
        options = options.split(", ")
        await ctx.send("**{}**".format(random.choice(options)))

    @commands.command(pass_context=True)
    async def flip(self, number: int):
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
        results = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yep.",
               "Signs point to yes.", "Reply hazy. Try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
               "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        await ctx.send(random.choice(results))

    
    @commands.command(pass_context=True)
    async def rps(self, choice: str):
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
                
            


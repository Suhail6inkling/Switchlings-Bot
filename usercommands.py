import discord
from discord.ext import commands
import asyncio
import random
from SwifflingBot import TOKEN, badwords1, badwords2, noroles, channels, SSinfo, hangmanwords, allowedwords, TCK, TCS, TATC, TATS,

(server, starttime, person, ownrole, grouprole, welcomechat, swifflingbotchat, warningschat, bot, defmaster, api) = onlinestuff()
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
    async def leave(self, ctx):
        if ctx.author == person:
           await person.remove_roles(ownrole)
           await person.remove_roles(grouprole)
           await ctx.message.add_reaction("✅")

    @commands.command(pass_context=True)
    async def join(self, ctx):
         if ctx.author == person:
           await person.add_roles(ownrole)
           await person.add_roles(grouprole)
           await ctx/message.add_reaction("✅")

    @commands.command(pass_context=True)
    async def help(self, ctx):
        await ctx.message.add_reaction("✅")
        if "Mods" in [role.name for role in ctx.author.roles]:
            try:
                await ctx.author.send("""Hello there, moderator! Thanks again for being an amazing mod! As you're aware, I'm the **Switchling Bot**, designed for the **Switchlings Plaza!** This is what I can do for everyone:
```md
<s.help> - That... just displays... this... mess- oh never mind.
<s.userinfo (@mention)> - Gives you information about the specific user.
<s.randomfact (Switchling name)> - Gives you a random fact about one of us! {In Progress}
<s.switchling (Switchling name)> - Gives you the basic facts about one of us!

<s.randomchoice (comma-separated values)> - Randomly chooses from given options.
<s.flip (number of coins)> - Flips a specific amount of coins.
<s.magic8ball> - Ask me a question!
<s.playgame (game)> - Let's play a game!```


And this is what I can do exclusively for you guys:""")
                await ctx.author.send("""
```md
<s.mute (@mention(s))> - Mutes a specific person / specific people.
<s.unmute (@mention(s))> - Unmutes a specific person / specific people.
<s.timeout (@mention seconds)> - Mutes a specific person for a period of time.
<s.warn (@mention reason)> - Warns a specific person and sends a message to warnings.
<s.editwarningnumber (@mention, number)> - Edits the amount of warnings that specific person has, removes all warnings if the number is 0.
<s.kick (@mention)> - Kicks a specific person.
<s.ban (@mention)> - Bans a specific person.
<s.prune (number of messages)> - Deletes a select number of messages.
<s.print (#channel message)> - Prints said message to the desired channel.```



Please note that some of these commands are a work in progress and may not work.""")
##To add##
#<s.giveroles (@mention, role1, role2, etc)> - Gives a specific person a role / roles.
#<s.removeroles (@mention, role1, role2, etc)> - Removes a role / roles from a specific person
            except discord.errors.Forbidden:
                await ctx.send("You must have DMs from server members allowed!")
        else:
            try:
                await ctx.author.send("""Hello there! My name is **Switchling Bot**! I'm the bot designed for the **Switchlings Plaza!**. This is what I *should be able to* do: [I'm a WIP so apologies if things may not work]
```md
<s.help> - That... just displays... this... mess- oh never mind.
<s.userinfo (@mention)> - Gives you information about the specific user.
<s.randomfact (Switchling name)> - Gives you a random fact about one of us! {In Progress}
<s.switchling (Switchling name)> - Gives you the basic facts about one of us!

<s.randomchoice (comma-separated values)> - Randomly chooses from given options.
<s.flip (number of coins)> - Flips a specific amount of coins.
<s.magic8ball> - Ask me a question!```
        


Please note that some of these commands are a work in progress and may not work.""")
            except discord.errors.Forbidden:
                await ctx.send("You must have DMs from server members allowed!")

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
            await ctx.send("WIP")

    @switchlings.command()
    async def Minty12inkling(self, ctx):
            await ctx.send("WIP")


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
        t = api.GetUserTimeline(screen_name="splatoon2maps", count=3)
        tweets = [i.AsDict() for i in t]
        for tweet in tweets:
            if "Turf War" in tweet["text"]:
                map1 = tweet["text"].split("Turf War maps: ")[1]
                map1 = map1.split(" &amp;")[0]
                map2 = tweet["text"].split("&amp; ")[1]
                map2 = map2.split(" #Splatoon2")[0]
                map1photo = tweet["media"][0]["media_url"]
                map2photo = tweet["media"][1]["media_url"]
                embed = discord.Embed(title = "Regular Battle", description="""
**Mode:**
Turf War

**Maps:**
{}
{}""".format(map1,map2),colour=0x19D619)
                await ctx.send(embed=embed)

    @stages.command()
    async def ranked(self, ctx):
            t = api.GetUserTimeline(screen_name="splatoon2maps", count=3)
            tweets = [i.AsDict() for i in t]
            for tweet in tweets:
                if "Ranked Battle" in tweet["text"]:
                    mode = tweet["text"].split("Ranked Battle maps — ")[1]
                    mode = mode.split(": ")[0]
                    map1 = tweet["text"].split(": ")[1]
                    map1 = map1.split(" &amp;")[0]
                    map2 = tweet["text"].split("&amp; ")[1]
                    map2 = map2.split(" #Splatoon2")[0]
                    map1photo = tweet["media"][0]["media_url"]
                    map2photo = tweet["media"][1]["media_url"]
                    embed = discord.Embed(title = "Ranked Battle", description="""
    **Mode:**
    {}

    **Maps:**
    {}
    {}""".format(mode,map1,map2),colour=0xF44910)
                    await ctx.send(embed=embed)


    @stages.command()
    async def league(self, ctx):
            t = api.GetUserTimeline(screen_name="splatoon2maps", count=3)
            tweets = [i.AsDict() for i in t]
            for tweet in tweets:
                if "League Battle" in tweet["text"]:
                    mode = tweet["text"].split("League Battle maps — ")[1]
                    mode = mode.split(": ")[0]
                    map1 = tweet["text"].split(": ")[1]
                    map1 = map1.split(" &amp;")[0]
                    map2 = tweet["text"].split("&amp; ")[1]
                    map2 = map2.split(" #Splatoon2")[0]
                    map1photo = tweet["media"][0]["media_url"]
                    map2photo = tweet["media"][1]["media_url"]
                    embed = discord.Embed(title = "League Battle", description="""
    **Mode:**
    {}

    **Maps:**
    {}
    {}""".format(mode,map1,map2),colour=0xEE2D7C)
                    await ctx.send(embed=embed)
            
    @commands.command(pass_context=True)
    async def splatnet(self, ctx):
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
     client.add_cog(UserCommands(client))  
                
            


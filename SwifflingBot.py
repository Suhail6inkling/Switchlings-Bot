import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio, random, os, csv

try:
    from config import TOKEN, badwords1, badwords2, noroles, channels, SSinfo, categories
except ModuleNotFoundError:
    TOKEN = os.environ['TOKEN']
    badwords1 = (os.environ['badwords1']).split(",")
    badwords2 = (os.environ["badwords2"]).split(",")
    noroles = (os.environ["noroles"]).split(",")
    channels = (os.environ["channels"]).split(",")
    SSinfo = (os.environ["SSinfo"]).split(",")
    categories = (os.environ["categories"]).split(",")
    
Client = discord.Client()
prefix = "s."
client = commands.Bot(command_prefix=prefix)

@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(activity = discord.Game(name="Say s.help"))
    global server, person, ownrole, grouprole, welcomechat, swifflingbotchat, warningschat, warning, bot
    server = client.get_guild(413113734303580171)
    person = discord.utils.get(server.members, name="Government Guinea Pig")
    bot = discord.utils.get(server.members, name="Switchlings Bot")
    ownrole = discord.utils.get(server.roles, name = "Suhail6inkling")
    grouprole = discord.utils.get(server.roles, name = "The Switchlings")
    welcomechat = discord.utils.get(server.channels, name = "welcome")
    swifflingbotchat = discord.utils.get(server.channels, name = "swifflingbotchat")
    warningschat = discord.utils.get(server.channels, name = "warnings")
    file = open("warning.csv","r")
    reader = csv.reader(file)
    warning = list(reader)
    print(warning)
    for x in warning:
        if x == []:
            warning.remove(x)
        else:
            x[1] = int(x[1])


@client.event
async def on_message(message):
    if message.content.startswith("s,exception s."):
        print("Hi")
        if message.author == person:
            message.content=(message.content.split("s,exception "))[1]
            print(message.content)
            noexception = False
            await on_message(message)
            noexception = True
        else:
            pass
    if message.content.startswith("s.exception"):
        if message.author == person:
            return
        else:
            pass"""
    """global badwords1, swifflingbotchat, warningschat, bot#, noexception
    for word in badwords1:
        if word in (message.content.lower()) and message.author != bot:#and noexception:
            await message.channel.send("{}, Please don't joke about sensitive topics. It could lead to a perm ban. If you're serious about this, don't hesitate to DM a Switchling and they can help you.".format(message.author.mention))
            message.delete()
            reason = "for talking about sensitive content [Automated Warning] [rape]"
            await givewarning(message.author.mention, reason)
            return
    for word in badwords2:
        if word in (message.content.lower()) and message.author != bot:# and noexception:
            await message.channel.send("{}, Please don't joke about sensitive topics. It could lead to a perm ban. If you're serious about this, don't hesitate to DM a Switchling and they can help you.".format(message.author.mention))
            message.delete()
            reason = "for talking about sensitive content [Automated Warning] [suicide]"
            await givewarning(message.author.mention, reason)
            return
    print(badwords1)
    print(badwords2)
    print(message.content)
    for a in badwords1:
        print(a)
    if message.content.startswith("s.ping"):
        await message.channel.send("Pong!")
        await message.add_reaction("✅")
        return
    if message.content.startswith("s.warn"):
        warninger = message.mentions
        member = warninger[0]
        a = message.content.split(" ")
        a.remove(a[0])
        a.remove(a[0])
        reason = ""
        for b in a:
            reason = "{}{} ".format(reason,b)
        if "Mods" in [a.name for a in message.author.roles]:
            if "Mods" in [a.name for a in member.roles]:
                await message.channel.send("You can't warn a fellow Mod!")
                return
            elif "NPCs" in [a.name for a in member.roles]:
                await message.channe;send("You can't warn a Bot!")
                return
            await message.add_reaction("✅")
            await givewarning(member.mention, reason)
        else:
            await message.channel.send("You're not a Mod!")
        return

    if message.content.startswith("s.editwarningnumber"):
        warninger = message.mentions
        warninger = warninger[0]
        a = message.content.split(" ")
        a.remove(a[0])
        a.remove(a[0])
        num = int(a[0])
        nowarnings = True
        for w in warning:
            if warninger.mention in w:
                nowarnings = False
                if num == 0:
                    warning.remove(w)
                else:
                    w[1] = num
        if nowarnings:
            if num == 0:
                pass
                await message.channel.send("This person didn't have any warnings to begin with!")
            else:
                warning.append([warninger.mention, num])
        await message.add_reaction("✅")
        await warningwrite()
        return
    if message.content.startswith("s.gimmeeveryrole"):
        if message.author == person:
            roleid = []
            for a in noroles:
                roleid.append(discord.utils.get(server.roles, name = a))
            for rolename in server.roles:
                if rolename not in roleid:
                    try:
                        await person.add_roles(rolename)
                    except:
                        print(rolename.name)
            await message.add_reaction("✅")
        else:
            await message.channel.send("Only works for Suhail6inkling")
        return
    if message.content.startswith("s.leave"):
        if message.author == person:
            await person.remove_roles(ownrole)
            await person.remove_roles(grouprole)
            await message.add_reaction("✅")
        return
    if message.content.startswith("s.join"):
       if message.author == person:
           await person.add_roles(ownrole)
           await person.add_roles(grouprole)
           await message.add_reaction("✅")
       return
    if message.content.startswith("s.help"):
        await message.add_reaction("✅")
        if "Mods" in [role.name for role in message.author.roles]:
            try:
                await message.author.send("""Hello there, moderator! Thanks again for being an amazing mod! As you're aware, I'm the **Switchling Bot**, designed for the **Switchlings Plaza!** This is what I can do for everyone:
```md
<s.help> - That... just displays... this... mess- oh never mind.
<s.userinfo (@mention)> - Gives you information about the specific user.
<s.randomfact (Switchling name)> - Gives you a random fact about one of us! {In Progress}
<s.switchling (Switchling name)> - Gives you the basic facts about one of us!

<s.randomchoice (comma-separated values)> - Randomly chooses from given options.
<s.flip (number of coins)> - Flips a specific amount of coins.
<s.magic8ball> - Ask me a question!```


And this is what I can do exclusively for you guys:""")
                await message.author.send("""
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
#<s.removeroles (@mention, role1, role2, etc)> - Removes a role / roles from a specific person/
            except discord.errors.Forbidden:
                await message.channel.send("You must have DMs from server members allowed!")
        else:
            try:
                await message.author.send("""Hello there! My name is **Switchling Bot**! I'm the bot designed for the **Switchlings Plaza!**. This is what I *should be able to* do: [I'm a WIP so apologies if things may not work]
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
                await message.channel.send("You must have DMs from server members allowed!")
        return     
    if message.content.startswith("s.userinfo"):
        member = message.mentions
        member = member[0]
        embed = discord.Embed(description=("""**Username:**           {}
**ID:**                    {}
**Status**                {}
**Highest Role**        {}
**Join Date:**           {}""".format(member.name, member.id, member.status, member.top_role, member.joined_at)))
        await message.channel.send(embed=embed)
        return
    if message.content.startswith("s.switchling Seven19inkling"):
        embed = discord.Embed(title="Seven19inkling:",description=SSinfo[0],colour=0x3470db)
        embed.set_thumbnail(url="https://media.discordapp.net/attachments/380910479276638225/380914087262945280/Seven_4.0.png?width=888&height=500")
        await message.channel.send(embed=embed)
        return 
    if message.content.startswith("s.switchling Smol4inkling"):
        embed = discord.Embed(title="Smol4inkling:",description=SSinfo[1],color=0xff8e8e)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/380910479276638225/380914146960605184/Smol4.png")
        await message.channel.send(embed=embed)
        return
    if message.content.startswith("s.switchling Suhail6inkling"):
        embed = discord.Embed(title="Suhail6inkling:",description=SSinfo[2],color=0x00ff00)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/380910479276638225/380914198240034841/Suhail_2.png")
        await message.channel.send(embed=embed)
        return
    if message.content.startswith("s.switchling Def0octoling"):
        embed = discord.Embed(title="Def0octoling:",description=SSinfo[3],color=0x990000)
        embed.set_thumbnail(url="")
        await message.channel.send(embed=embed)
        return
    if message.content.startswith("s.switchling"):
        await message.channel.send("""Please select with one of the following:
```md
<s.switchling Seven19inkling>
<s.switchling Smol4inkling>
<s.switchling Suhail6inkling>
<s.switchling Def0octoling>```""")
        return
    if message.content.startswith("s.randomchoice"):
        options = ((message.content.split("s.randomchoice "))[1]).split(", ")
        result = random.choice(options)
        await message.channel.send("**{}**".format(result))
        return
    if message.content.startswith("s.flip"):
        number = int((message.content.split("s.flip "))[1])
        result=""
        for c in range(0,number):
            if c != 0:
                result="{}\n".format(result)
            i = random.randint(0,1)
            if i == 0:
                result=result+"Tails"
            else:
                result=result+"Heads"
        await message.channel.send("**{}**".format(result))
        return
    if message.content.startswith("s.magic8ball"):
        results = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yep.",
               "Signs point to yes.", "Reply hazy. Try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.",
               "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
        await message.channel.send(random.choice(results))
        return
    if message.content.startswith("s.mute"):
        if "Mods" in [role.name for role in message.author.roles]:
            members = message.mentions
            for member in members:
                if "Mods" not in [role.name for role in member.roles]:
                    for ID in channels:
                        channel = client.get_channel(ID)
                        perms = discord.PermissionOverwrite()
                        perms.send_messages = False
                        await channel.set_permissions(member, overwrite=perms)
                    await message.channel.send("{} has been muted".format(member.mention))
                else:
                    await message.channel.send("You can't mute a fellow mod!")
        else:
            await message.channel.send("You need to be a Mod to do this!")
        return
    if message.content.startswith("s.unmute"):
        if "Mods" in [role.name for role in message.author.roles]:
            members = message.mentions
            for member in members:
                if "Mods" not in [role.name for role in member.roles]:
                    for ID in channels:
                        channel = client.get_channel(ID)
                        await channel.set_permissions(member, overwrite=None)
                    await message.channel.send("{} has been unmuted".format(member.mention))
                else:
                    await message.channel.send("You can't unmute a fellow mod!")
        else:
            await message.channel.send("You need to be a Mod to do this!")
        return
    if message.content.startswith("s.open"):
        if "The Switchlings" in [role.name for role in message.author.roles]:
            permashut = False
        return

    
    if message.content.startswith("s.lockdown"):
        if "The Switchlings" in [role.name for role in message.author.roles]:
            permashut = True
            a = message.content.split("s.lockdown ")
            try:
                secs = int(a[1])
            except:
                secs = "indefinite"
            for ID in channels:
                        channel = client.get_channel(ID)
                        perms = discord.PermissionOverwrite()
                        perms.send_messages = False
                        await channel.set_permissions(message.guild.default_role, overwrite=perms)
            await message.channel.send("The Switchlings Plaza! has been shut.")
            if secs == "indefinite":
                while True:
                    asyncio.sleep(1)
                    if permashut == False:
                        break
            for i in range(0, secs):
                asyncio.sleep(1)
                if permashut == False:
                    break
            for ID in channels:
                        channel = client.get_channel(ID)
                        perms = discord.PermissionOverwrite()
                        perms.send_messages = True
                        await channel.set_permissions(message.guild.default_role, overwrite=perms)
            await message.channel.send("The Switchlings Plaza! is now open!")
            return
    if message.content.startswith("s.timeout"):
        timeouter = message.mentions
        timeouter = timeouter[0]
        a = message.content.split(" ")
        a.remove(a[0])
        a.remove(a[0])
        secs = int(a[0])
        if "Mods" in [role.name for role in message.author.roles]:
            if "Mods" not in [role.name for role in timeouter.roles]:
                 for ID in channels:
                   channel = client.get_channel(ID)
                   perms = discord.PermissionOverwrite()
                   perms.send_messages = False
                   await channel.set_permissions(timeouter, overwrite=perms)
                 await ctx.send("{} has been muted for {} seconds".format(timeouter.mention, secs))
                 for i in range(0, secs):
                    await asyncio.sleep(1)
                 for ID in channels:
                    channel = client.get_channel(ID)
                    await channel.set_permissions(timeouter, overwrite=None)
                 await message.channel.send("{} has been unmuted after a timeout".format(timeouter.mention))
            else:
                await message.channel.send("You cannot timeout a fellow mod!")
        else:
            await ctx.send("You need to be a Mod to do this!")
        return
    if message.content.startswith("s.kick"):
        kickers = message.mentions
        if "Mods" in [role.name for role in message.author.roles]:
            for kicker in kickers:
                if "Mods" in [role.name for role in kicker.roles]:
                    await message.channel.send("You can't kick out a fellow Mod!")
                else:
                    await message.guild.kick(kicker)
                    await message.channel.send("{} has been kicked".format(kicker.name))
        else:
            await message.channel.send("You need to be a mod to do this!")
        return
    if message.content.startswith("s.ban"):
        banners = message.mentions
        if "Mods" in [role.name for role in message.author.roles]:
            for banner in banners:
                if "Mods" in [role.name for role in banner.roles]:
                    await message.channel.send("You can't ban a fellow Mod!")
                else:
                    await message.guild.ban(banner)
                    await message.channel.send("{} has been banned".format(banner.name))
        else:
            await message.channel.send("You need to be a mod to do this!")
        return
    if message.content.startswith("s.prune"):
        if "Mods" in [role.name for role in message.author.roles]:
            a = message.content.split(" ")
            a = int(a[1])
            await message.channel.purge(limit=a+1,check=None,bulk=True)
            await message.channel.send("{} messages have been cleared".format(a),delete_after=3)
        return
    if message.content.startswith("s.print"):
        if "Mods" in [role.name for role in message.author.roles]:
            x = message.content.split(" ")
            textchannel = (message.channel_mentions)[0]
            tosend = ""
            x.remove(x[0])
            x.remove(x[0])
            for y in x:
                tosend = "{} {}".format(tosend,y)
            await textchannel.send("{}".format(tosend))
            await message.add_reaction("✅")
        return
    if message.content.startswith("s."):
        await message.add_reaction("❌")
        return
    if message.content.startswith("S."):
        await message.add_reaction(u"\U0001F1F1")
        await message.add_reaction(u"\U0001F1F4")
        await message.add_reaction(u"\U0001F1FC")
        await message.add_reaction(u"\U0001F1EA")
        await message.add_reaction(u"\U0001F1F7")
        await message.add_reaction(u"\U0001F1E8")
        await message.add_reaction(u"\U0001F1E6")
        await message.add_reaction(u"\U0001F1F8")
        return
        
        
    
async def givewarning(user, reason):
    global warningschat, swifflingbotchat, warning
    firstwarning = True
    for warningee in warning:
        if  warningee[0] == user:
            firstwarning = False
            warningee[1]+=1
            num = warningee[1]
            if (str(num).endswith("1")) and ((str(num).endswith("11"))==False):
                ending = "st"
            elif (str(num).endswith("2")) and ((str(num).endswith("12"))==False):
                ending = "nd"
            elif (str(num).endswith("3")) and ((str(num).endswith("13"))==False):
                ending = "rd"
            else:
                ending = "th"
    if firstwarning:
        warningee = [user, 1]
        warning.append(warningee)
        ending = "st"
    if reason.endswith("[rape]"):
        h = reason.split("[rape]")
        await warningschat.send("{}{} warning for {} {}".format(warningee[1],ending,user,h[0]))
        embed = discord.Embed(title="Person Warned", description=("""
User:
{}

Warning No.:
{}

Reason:
{}""".format(user,warningee[1],reason)),colour=0x0000ff)
    elif reason.endswith("[suicide]"):
        h = reason.split("[suicide]")
        await warningschat.send("{}{} warning for {} {}".format(warningee[1],ending,user,h[0]))
        embed = discord.Embed(title="Person Warned", description=("""
User:
{}

Warning No.:
{}

Reason:
{}""".format(user,warningee[1],reason)),colour=0x0000ff)
    else:
        await warningschat.send("{}{} warning for {} {}".format(warningee[1],ending,user,reason))
        embed = discord.Embed(title="Person Warned", description=("""
User:
{}

Warning No.:
{}

Reason:
{}""".format(user,warningee[1],reason)),colour=0x0000ff)
        
    await swifflingbotchat.send(embed=embed)
    if warningee[1] == 3:
        await swifflingbotchat.send("```Would be banned at this point```")
    await warningwrite()

async def warningwrite():
    file = open("warning.csv","w")
    writer = csv.writer(file)
    for a in warning:
        try:
            a[0] = a[0].mention
        except:
            pass
        writer.writerow(a)
    file.close()

@client.event
async def on_member_remove(member):
    global welcomechat, swifflingbotchat
    await welcomechat.send("**{}** has been splatted and has left the server. :(".format(member.name))
    embed = discord.Embed(title="Member leave",description=("{}, [ID = {}]".format(member.mention,member.id)),colour=0xff0000)
    avatar = member.avatar_url_as(format="jpg",size=512)
    embed.set_thumbnail(url=avatar)
    await swifflingbotchat.send(embed=embed)

@client.event
async def on_member_join(member):
    global welcomechat, swifflingbotchat
    await welcomechat.send("{}, Welcome to the Switchlings Server! Make sure you read the #rules and have an amazing time here!".format(member.mention))
    embed = discord.Embed(title="Member join", description=("{}, [ID = {}]".format(member.mention,member.id)),colour=0x00ff00)
    avatar = member.avatar_url_as(format="jpg",size=512)
    embed.set_thumbnail(url=avatar) 
    await swifflingbotchat.send(embed=embed)
    

async def KeepAwake():
    await asyncio.sleep(1500)
    print("Still awake")
"""    
async def flash():
    await client.wait_until_ready()
    server = client.get_guild(413113734303580171)
    botrole = discord.utils.get(server.roles, name="The Switchlings Bot")
    colours = [0x3470db, 0xff8e8e, 0x00ff00, 0x990000]
    while True:
        for color in colours:
            asyncio.sleep(500)
            await botrole.edit(colour=discord.Colour(color))
            asyncio.sleep(500)

client.loop.create_task(flash())
"""
client.loop.create_task(KeepAwake())
client.run(TOKEN)

    

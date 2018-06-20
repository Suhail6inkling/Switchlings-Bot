"These are from older versions of the Switchlings Bot that are unnecessary at the moment but may be added again later"


        """if len(alphashort) < 4:
            lenalpha = 4
        else:
            lenalpha = len(alphashort)
        if len(bravoshort) < 4:
            lenbravo = 4
        else:
            lenbravo = len(bravoshort)
        tableformat1 = "{}        {}        {}".format(alphashort,"         ",bravoshort)
        aformat = ""
        for x in range(0,lenalpha):
            aformat+="-"
        bformat = ""
        for x in range(0,lenalpha):
            bformat+="-"
        tableformat2 = "{}--------{}--------{}".format(aformat,"----------",bformat)
        aformat = str(float(ourresult["rates"]["vote"]["alpha"]/100))
        for x in range(4,lenalpha):
            aformat+=" "
        bformat = str(float(ourresult["rates"]["vote"]["bravo"]/100))
        for x in range(4,lenbravo):
            bformat+=" "
        tableformat3 = "{}        {}        {}".format(aformat,"Popularity",bformat)
        
        aformat = str(float(ourresult["rates"]["solo"]["alpha"]/100))
        for x in range(4,lenalpha):
            aformat+=" "
        bformat = str(float(ourresult["rates"]["solo"]["bravo"]/100))
        for x in range(4,lenbravo):
            bformat+=" "

        tableformat4 = "{}        {}        {}".format(aformat," Solo Wins",bformat)       
        aformat = str(float(ourresult["rates"]["team"]["alpha"]/100))
        for x in range(4,lenalpha):
            aformat+=" "
        bformat = str(float(ourresult["rates"]["team"]["bravo"]/100))
        for x in range(4,lenbravo):
            bformat+=" "
        tableformat5 = "{}        {}        {}".format(aformat," Team Wins",bformat)
        aformat = str(alphacount)
        for x in range(1,lenalpha):
            aformat+=" "
        bformat= str(bravocount)
        for x in range(1,lenbravo):
            bformat+=" "
        tableformat6 = "{}        {}        {}".format(alphacount,"   Total  ",bravocount)"""


"""
        try:
            await ctx.author.send("Hello there! My name is **Switchlings Bot**, made specifically for the **Switchlings Plaza!**. Here is what I can do. [Please note that I'm a WIP so not all commands work]

```md

Splatoon
<s.stages regular> - See what Turf War maps are on for the next three rotations
<s.stages ranked> - See what's on Ranked Battle for the next three rotations
<s.stages league> - See what's on League Battle for the next three rotations
<s.splatnet> - See what's in the SplatNet shop!```")

            await ctx.author.send("```md
Fun
<s.rps (Rock, Paper or Scissors)> - Challenge me IF YOU DARE!
<s.randomchoice (comma-separated values)> - Randomly chooses from given options.
<s.flip (number of coins)> - Flips a specific amount of coins.
<s.magic8ball> - Ask me a question!```")
            
            await ctx.author.send("```md

Other
<s.help> - Displays this message
<s.ping> - Check how long this bot takes to respond
<s.botstatus> - Check how long the bot's been running for!
<s.userinfo @mention> - Check generic user information for a specific person
<s.switchlings Switchling> - Gain more information about one of the 5 Switchlings!```")
            await ctx.send("Documentation has been sent to your DMs!")
        except:
            await ctx.send("Please enable Direct Messages from server members!")
"""







"""
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
            await message.channel.send("Only works for Suhail6inkling")"""

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


##
##    @commands.commands(pass_context=True)
##    async def test(self, ctx, a: str):
##        if a == "hangman":
##            print(hangman)
##            await person.send(hangman)





##    await sql.open()
##    cur.execute("SELECT * FROM warnings")
##    warning = cur.fetchall()
##    for x in range(0,len(warning)):
##        warning[x] = list(warning[x])
##    cur.execute("DELETE FROM warnings")
##    for x in range(0, len(warning)):
##        a = warning[x][0]
##        a = ((a.split("<")[1]).split(">")[0])
##        p = discord.Member(a)
##        warning[x][0]=str(p.id)
##        await sql.add(warning[x])
##
##
##
##    hangmanman = ["https://cdn.discordapp.com/attachments/397821075150602242/443075712514261002/hangman0.png","https://cdn.discordapp.com/attachments/397821075150602242/443074582539141120/hangman1.png","https://cdn.discordapp.com/attachments/397821075150602242/443074585156386816/hangman2.png","https://cdn.discordapp.com/attachments/397821075150602242/443074587245412363/hangman3.png","https://cdn.discordapp.com/attachments/397821075150602242/443074588721545217/hangman4.png","https://cdn.discordapp.com/attachments/397821075150602242/443075307939954688/hangman5.png","https://cdn.discordapp.com/attachments/397821075150602242/443074594748760074/hangman6.png"]
##    hangman = [False]
##
##    """if message.content.startswith("s,exception s."):
##        print("Hi")
##        if message.author == person:
##            message.content=(message.content.split("s,exception "))[1]
##            print(message.content)
##            noexception = False
##            await on_message(message)
##            noexception = True
##        else:
##            pass
##    if message.content.startswith("s.exception"):
##        if message.author == person:
##            return
##        else:
##            pass"""
##
##
##await givewarning(message.author.id, reason)
##
##            if a == "sql":
##                await sql.open()
##                cur.execute("SELECT * FROM warnings")
##                p = cur.fetchall()
##                print(p)
##                await person.send(p)
##                await sql.close()
##
##            if a == "warning":
##                print(warning)
##                await person.send(warning)
##
##
##    if message.content.startswith("s.warn"):
##        warninger = message.mentions
##        member = warninger[0]
##        a = message.content.split(" ")
##        a.remove(a[0])
##        a.remove(a[0])
##        reason = ""
##        for b in a:
##            reason = "{}{} ".format(reason,b)
##        if "Mods" in [a.name for a in message.author.roles]:
##            if "Mods" in [a.name for a in member.roles]:
##                await message.channel.send("You can't warn a fellow Mod!")
##                return
##            elif "NPCs" in [a.name for a in member.roles]:
##                await message.channe;send("You can't warn a Bot!")
##                return
##            await message.add_reaction("✅")
##            await givewarning(member.id, reason)
##        else:
##            await message.channel.send("You're not a Mod!")
##        return
##
##    if message.content.startswith("s.editwarningnumber"):
##        if "Mods" in [role.name for role in message.author.roles]:
##            warninger = message.mentions
##            warninger = warninger[0]
##            a = message.content.split(" ")
##            a.remove(a[0])
##            a.remove(a[0])
##            num = int(a[0])
##            nowarnings = True
##            for w in warning:
##                if warninger.mention in w:
##                    nowarnings = False
##                    if num == 0:
##                        warning.remove(w)
##                        warningeelist = [warninger.mention,w[1]]
##                        await sql.remove(warningeelist)
##                    else:
##                        w[1] = num
##                        warningeelist = [warninger.mention,num]
##                        await sql.edit(warningeelist)
##                    
##            if nowarnings:
##                if num == 0:
##                    pass
##                    await message.channel.send("This person didn't have any warnings to begin with!")
##                else:
##                    warning.append([warninger.mention, num])
##                    warningeelist = [warninger.mention, num]
##                    await sql.add(warningeelist)
##            await message.add_reaction("✅")
##            return
##
##
##async def givewarning(user, reason):
##    global warningschat, swifflingbotchat, warning
##    firstwarning = True
##    for warningee in warning:
##        if  warningee[0] == user:
##            firstwarning = False
##            warningee[1]+=1
##            num = warningee[1]
##            warningeelist = warningee
##            if (str(num).endswith("1")) and ((str(num).endswith("11"))==False):
##                ending = "st"
##            elif (str(num).endswith("2")) and ((str(num).endswith("12"))==False):
##                ending = "nd"
##            elif (str(num).endswith("3")) and ((str(num).endswith("13"))==False):
##                ending = "rd"
##            else:
##                ending = "th"
##            warningeelist = warningee
##            await sql.edit(warningeelist)
##    if firstwarning:
##        warningee = [user, 1]
##        warningeelist = warningee
##        warning.append(warningee)
##        ending = "st"
##        await sql.add(warningeelist)
##    if reason.endswith("[rape]"):
##        h = reason.split("[rape]")
##        await warningschat.send("{}{} warning for {} {}".format(warningee[1],ending,user,h[0]))
##        embed = discord.Embed(title="Person Warned", description=("""
##User:
##{}
##
##Warning No.:
##{}
##
##Reason:
##{}""".format(user,warningee[1],reason)),colour=0x0000ff)
##    elif reason.endswith("[suicide]"):
##        h = reason.split("[suicide]")
##        await warningschat.send("{}{} warning for {} {}".format(warningee[1],ending,user,h[0]))
##        embed = discord.Embed(title="Person Warned", description=("""
##User:
##{}
##
##Warning No.:
##{}
##
##Reason:
##{}""".format(user,warningee[1],reason)),colour=0x0000ff)
##    else:
##        await warningschat.send("{}{} warning for {} {}".format(warningee[1],ending,user,reason))
##        embed = discord.Embed(title="Person Warned", description=("""   
##User:
##{}
##
##Warning No.:
##{}
##
##Reason:
##{}""".format(user,warningee[1],reason)),colour=0x0000ff)
##        
##    await swifflingbotchat.send(embed=embed)
##    if warningee[1] == 3:
##        await swifflingbotchat.send("```Would be banned at this point```")
##
##class sql():
##    async def edit(warningeelist):
##        await sql.open()
##        cur.execute("UPDATE warnings SET num = %s WHERE mention = %s",(warningeelist[1],warningeelist[0]))
##        await sql.close()
##    async def add(warningeelist):
##        await sql.open()
##        cur.execute("INSERT INTO warnings VALUES (%s, %s)",(warningeelist[0],warningeelist[1]))
##        await sql.close()
##    async def remove(warningeelist):
##        await sql.open()
##        cur.execute("DELETE FROM warnings WHERE mention = %s AND num = %s",(warningeelist[0],warningeelist[1]))
##        await sql.close()
##    
##    async def open():
##        global con, cur
##        dburl = os.environ["DATABASE_URL"]
##        con = psycopg2.connect(dburl, sslmode="require")
##        cur = con.cursor()
##
##    async def close():
##        con.commit()
##        cur.close()
##        con.close()
##    
##async def drawhangman(messagechannel, dashedword, printguessedletters, hangperson):
##    await messagechannel.send("""
##Word: **{}**
##
##Letters guessed: *{}*
##
##{}""".format(dashedword, printguessedletters, hangperson))
##
##
## if message.content.startswith("s.playgame hangman"):
##        if hangman[0] == True:
##            await message.channel.send("There's already a hangman game going on!")
##            return
##        else:
##            word = random.choice(hangmanwords)
##            dashedword = ""
##            printdashedword = ""
##            for a in range(0, len(word)):
##                dashedword = ("{}-".format(dashedword))
##                printdashedword=("{}  -".format(printdashedword))
##            guessedletters = []
##            printguessedletters = ""
##            hangmanstatus = 0
##            hangmantime = 0
##            hangperson = hangmanman[hangmanstatus]
##            await drawhangman(message.channel, printdashedword, printguessedletters, hangperson)
##            await message.channel.send("Use `<s.gl (letter)>` to guess a letter and `<s.gw (word)>` to guess the entire word!")
##            hangman = [True, message.author.mention, word, dashedword, printdashedword, guessedletters, printguessedletters, hangmanstatus]
##            while True:
##                await asyncio.sleep(1)
##                hangmantime+=1
##                print(hangmantime)
##                if hangmantime == 100:
##                    await message.channel.send("{}, you're hangman game has timed out".format(message.author.mention))
##                    hangman = [False]
##                if hangman[0] == False:
##                    break
##                
##        return
##            
##    if message.content.startswith("s.gl"):
##        if hangman[0] == False:
##            await message.channel.send("There is no hangman game going on!")
##            return
##        elif hangman[1] != message.author.mention:
##            await message.channel.send("You're not the person playing hangman right now!")
##            return
##        else:
##            hangmantime = 0
##            letter = message.content.split("s.gl ")[1]
##            if len(letter) != 1:
##                await message.channel.send("Please only give one letter!")
##                return
##            if letter in hangman[5]:
##                await message.channel.send("You've already guessed that letter!")
##                return
##            letter = letter.lower()
##            if letter in hangman[2]:
##                for c in range(0, len(hangman[2])):
##                    if hangman[2][c] == letter:
##                        hangman[4] = "{}{}{}".format(hangman[4][:(3*c)-1],letter,hangman[4][3*c:])
##                        hangman[3] = "{}{}{}".format(hangman[3][:c],letter,hangman[3][c+1:])
##                if hangman[3] == hangman[2]:
##                    await message.channel.send("Congratulations! You guessed the correct thing!")
##                    hangman = [False]
##                    return
##                if hangman[6] == "":
##                    hangman[6] = letter
##                else:
##                    hangman[6] = "{}, {}".format(hangman[6], letter)
##                hangman[5].append(letter)
##            else:
##                if hangman[6] == "":
##                    hangman[6] = letter
##                else:
##                    hangman[6] = "{}, {}".format(hangman[6], letter)
##                hangman[5].append(letter)
##                hangman[7]+=1
##                if hangman[7] == 6:
##                    await message.channel.send("You lose! The word was **{}**!".format(hangman[2]))
##                    hangman = [False]
##                    return
##            hangperson = hangmanman[hangman[7]]
##            await drawhangman(message.channel, hangman[4], hangman[6], hangperson)
##            return
##    if message.content.startswith("s.gw"):
##        if hangman[0] == False:
##            await message.channel.send("There is no hangman game going on!")
##            return
##        elif hangman[1] != message.author.mention:
##            await message.channel.send("You're not the person playing hangman right now!")
##            return
##        else:
##            hangmantime = 0
##            wordguess = (message.content.split("s.gw ")[1]).lower()
##            if wordguess == hangman[2]:
##                await message.channel.send("Congratulations! You guessed the word!")
##                hangman = [False]
##                return
##            else:
##                await message.channel.send("Incorrect!")
##                hangman[6]+=1
##                if hangman[6] == 6:
##                    await message.channel.send("You lose! The word was **{}**!".format(hangman[2]))
##                    hangman = [False]
##                    return
##            hangperson = hangmanman[hangman[6]]
##            await drawhangman(message.channel, hangman[3], hangman[5], hangperson)
##            return
##
##

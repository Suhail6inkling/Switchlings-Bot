import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio, random, os, time#, psycopg2
import urllib.parse as urlparse
import twitter
import sql

try:
    from config import TOKEN, badwords1, badwords2, noroles, channels, SSinfo, hangmanwords, allowedwords, TCK, TCS, TATC, TATS
except ModuleNotFoundError:
    TOKEN = os.environ['TOKEN']
    badwords1 = (os.environ['badwords1']).split(",")
    badwords2 = (os.environ["badwords2"]).split(",")
    noroles = (os.environ["noroles"]).split(",")
    channels = (os.environ["channels"]).split(",")
    SSinfo = (os.environ["SSinfo"]).split(",")
    hangmanwords = (os.environ["hangmanwords"]).split(",")
    allowedwords = (os.environ["allowedwords"]).split(",")
    TCK = os.environ["TCK"]
    TCS = os.environ["TCS"]
    TATC = os.environ["TATC"]
    TATS = os.environ["TATS"]
    
Client = discord.Client()   
prefix = "s."
client = commands.Bot(command_prefix=prefix)
startup_extensions=["usercommands","modcommands","splatooncommands","suhailcommands"]
client.remove_command("help")
global successful_extensions, failed_extensions
successful_extensions = []
failed_extensions = []


@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(activity = discord.Game(name="Say s.help"))
    await onlinestuff()

"""
id
switchcode
gender
skincolour
eyecolour
hairstyle
trousers
weapon

level
sz
tc
rm
cb

hat
hatsub1
hatsub2
hatsub3

shirt
shirtsub1
shirtsub2
shirtsub3

shoes
shoessub1
shoessub2
shoessub3"""
#cur = sql.open()
#cur.execute("INSERT INTO people (id) VALUES (%s)",[320366423052386334])
#sql.close()
sql.open()
people = sql.read()
sql.close()


async def onlinestuff():
    sbschat = (client.get_guild(413357189931991060)).get_channel(456118202666057729)
    person = (client.get_guild(413357189931991060)).get_member(131131701148647424)
    await sbschat.send("{} Online!".format(client.user.mention))
    global successful_extensions, failed_extensions
    if successful_extensions!=[]:
        for x in successful_extensions:
            await sbschat.send("Successfully loaded {}.py".format(x))
    if failed_extensions!=[]:
        for x in failed_extensions:
            await sbschat.send("""{} Failed to load {}.py
```{}: {}```""".format(person.mention, x[0], x[1], x[2]))

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = SAC.from_json_keyfile_name("SwifflingBot.json", scope)
cliente = gspread.authorize(creds)
sheet = cliente.open("Switchlings Bot Profile").sheet1
values=["ID", "Friend Code","Gender & Species","Skin Colour","Eye Colour","Hairstyle","Trousers","Weapon","Level","Splat Zone Rank","Tower Control Rank","Rainmaker Rank","Clam Blitz Rank","Hat Main","Hat Sub 1","Hat Sub 2","Hat Sub 3","Shirt Main","Shirt Sub 1","Shirt Sub 2","Shirt Sub 3","Shoes Main","Shoes Sub 1","Shoes Sub 2","Shoes Sub 3"]

a = people[199]
for x in a:
    x = str(x)
sheet.append_row(a)
a = people[200]
for x in a:
    x = str(x)




        
starttime = time.time()

@client.event
async def on_message(message):
    server = client.get_guild(413113734303580171)
    bot = discord.utils.get(server.members, name="Switchlings Bot")
    if message.guild == server:
        q = message.content.lower()
        for aword in allowedwords:
            if aword in q.lower():
                indexa = q.lower().index(aword)
                indexb = indexa+len(aword)
                zyx = q.split(q[indexa:indexb+1])
                p = ""
                for x in zyx:
                    p = "{}{}".format(p,x)
                q = p
        for word in badwords1:
            if word in (q.lower()) and message.author != bot:#and noexception:
                await message.channel.send("{}, Please don't joke about sensitive topics. It could lead to a perm ban. If you're serious about this, don't hesitate to DM a Switchling and they can help you.".format(message.author.mention))
                sbcchat = (client.get_guild(413357189931991060)).get_channel(456769518753021963)
                await sbcchat.send("{}: {}".format(message.author, message.content))
                await message.delete()
                return
        for word in badwords2:
            if word in (q.lower()) and message.author != bot:# and noexception:
                await message.channel.send("{}, Please don't joke about sensitive topics. It could lead to a perm ban. If you're serious about this, don't hesitate to DM a Switchling and they can help you.".format(message.author.mention))
                sbcchat = (client.get_guild(413357189931991060)).get_channel(456769518753021963)
                await sbcchat.send("{}: {}".format(message.author, message.content))
                await message.delete()
                return
    noservercommands=["s.mute","s.unmute","s.kick","s.ban","s.timeout","s.lockdown","s.open","s.test","s.leave","s.join","s.prune"]
    if message.content.split(" ")[0] in noservercommands and message.guild!=server:
        await message.channel.send("Those commands can only be used in **Switchlings Plaza!**")
        return
    try:
        await client.process_commands(message)
    except Exception as e:
        sbschat = (client.get_guild(413357189931991060)).get_channel(456118202666057729)
        await sbschat.send("{}: {}\n{}: {}".format(type(e).__name__,e,message.author, message.content))
    
        
        
         
@client.event
async def on_member_remove(member):
    server = client.get_guild(413113734303580171)
    if member.guild == server:
        welcomechat = discord.utils.get(server.channels, name = "welcome")
        swifflingbotchat = discord.utils.get(server.channels, name = "swifflingbotchat")
        await welcomechat.send("**{}** has been splatted and has left the server. :(".format(member.name))
        embed = discord.Embed(title="Member leave",description=("{}, [ID = {}]".format(member.mention,member.id)),colour=0xff0000)
        avatar = member.avatar_url_as(format="jpg",size=512)
        embed.set_thumbnail(url=avatar)
        await swifflingbotchat.send(embed=embed)
        cur = sql.open()
        cur.execute("DELETE FROM people WHERE id = (%s)",[member.id])
        sql.close()

@client.event
async def on_member_join(member):
    server = client.get_guild(413113734303580171)
    if member.guild == server:
        if member.id == 320366423052386334:
            return
        welcomechat = discord.utils.get(server.channels, name = "welcome")
        swifflingbotchat = discord.utils.get(server.channels, name = "swifflingbotchat")
        await welcomechat.send("{}, Welcome to the Switchlings Server! Make sure you read the #rules and have an amazing time here!".format(member.mention))
        embed = discord.Embed(title="Member join", description=("{}, [ID = {}]".format(member.mention,member.id)),colour=0x00ff00)
        avatar = member.avatar_url_as(format="jpg",size=512)
        embed.set_thumbnail(url=avatar) 
        await swifflingbotchat.send(embed=embed)
        cur = sql.open()
        cur.execute("INSERT INTO people (id) VALUES (%s)",[member.id])
        sql.close()
    

async def KeepAwake():
    await asyncio.sleep(1500)
    print("Still awake")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
            successful_extensions.append(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            failed_extensions.append([extension, (type(e).__name__), e])
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.loop.create_task(KeepAwake())
    client.run(TOKEN)

    

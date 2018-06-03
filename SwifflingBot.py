import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio, random, os, time#, psycopg2
import urllib.parse as urlparse
import twitter

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
startup_extensions=["usercommands","modcommands"]
client.remove_command("help")



@client.event
async def on_ready():
    print("Bot Online!")
    print("Name: {}".format(client.user.name))
    print("ID: {}".format(client.user.id))
    await client.change_presence(activity = discord.Game(name="Say s.help"))
    onlinestuff()

class onlinestuff():
    self.starttime = time.time()
    self.server = client.get_guild(413113734303580171)
    self.bottestingchat = discord.utils.get(server.channels, name = "bot-testing")
    self.person = server.get_member(131131701148647424)
    self.bot = discord.utils.get(server.members, name="Switchlings Bot")
    self.defmaster = client.get_user(331501118939201536)
    self.ownrole = discord.utils.get(server.roles, name = "Suhail6inkling")
    self.grouprole = discord.utils.get(server.roles, name = "The Switchlings")
    self.welcomechat = discord.utils.get(server.channels, name = "welcome")
    self.swifflingbotchat = discord.utils.get(server.channels, name = "swifflingbotchat")
    self.warningschat = discord.utils.get(server.channels, name = "warnings")
    self.api = twitter.Api(
        consumer_key=TCK,
        consumer_secret=TCS,
        access_token_key=TATC,
        access_token_secret=TATS)
    t = api.GetUserTimeline(screen_name="splatoon2maps", count=3)
    tweets = [i.AsDict() for i in t]
    
server = onlinestuff.server
starttime = onlinestuff.starttime
person = onlinestuff.person
ownrole = onlinestuff.ownrole
grouprole = onlinestuff.grouprole
welcomechat = onlinestuff.welcomechat
swifflingbotchat = onlinestuff.swifflingbotchat
warningschat = onlinestuff.warningschat
bot = onlinestuff.bot
defmaster = onlinestuff.defmaster
api = onlinestuff.api


@client.event
async def on_message(message):
    global starttime, badwords1, swifflingbotchat, warningschat, bot, hangman, hangmanman, allowedwords, defmaster, api#, noexception
    q = message.content
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
        if word in q.lower() and message.author != bot:#and noexception:
            await message.channel.send("{}, Please don't joke about sensitive topics. It could lead to a perm ban. If you're serious about this, don't hesitate to DM a Switchling and they can help you.".format(message.author.mention))
            await message.delete()
            return
    for word in badwords2:
        if word in (q.lower()) and message.author != bot:# and noexception:
            await message.channel.send("{}, Please don't joke about sensitive topics. It could lead to a perm ban. If you're serious about this, don't hesitate to DM a Switchling and they can help you.".format(message.author.mention))
            await message.delete()
            return                
    await client.process_commands(message)
    return
         
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

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

    client.loop.create_task(KeepAwake())
    client.run(TOKEN)

    

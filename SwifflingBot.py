import discord
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio, random, os, time#, psycopg2
import urllib.parse as urlparse
import twitter
from gsheets import SwitchlingsBotProfile as SBS
from gsheets import ListOfRanks as LOR

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



jmbphotos=["https://www.famousbirthdays.com/headshots/joseph-birlem-6.jpg",
"https://i1.wp.com/www.famedstar.com/wp-content/uploads/2018/01/Joey-Birlem-Height-Age-Weight-Wiki-Biography-Parents-Affairs-Siblings-Net-Worth.jpg?resize=700%2C605",
"https://a.wattpad.com/cover/106416278-352-k742150.jpg",
"https://pbs.twimg.com/profile_images/903368437233266688/WFd4BBeP_400x400.jpg",
"https://www.famousbirthdays.com/headshots/joseph-birlem-4.jpg",
"https://pbs.twimg.com/media/DGIWdmqUIAEakzs.jpg",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQERuVXJS_vKHe8blvWMbzHY9jhhMZSKyakMzUO9m5j6a-mvIsh",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSfzHo1bOkk5MK10uM6ua8oHdkGYpxaeXjz8h8bCUO9cboSUhfpjw"
"https://78.media.tumblr.com/68d5de0c64a9014e8501cd440d819a4b/tumblr_orv1rfQidc1w8rdaco1_1280.jpg",
"https://cdn.discordapp.com/attachments/442679711961710592/459795623852507146/unknown.png",
"https://cdn.discordapp.com/attachments/442679711961710592/455198565736775700/image.png",
"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRbrWWyzSKefPbBPa3_tZ77KuSYWEiyc-HDBP-Yv_Ju3V8KKc_9",
"https://a.wattpad.com/cover/104694240-288-k768814.jpg",
"https://cdn.discordapp.com/attachments/442679711961710592/459799278500577292/unknown.png",
"https://media.discordapp.net/attachments/422206454213115904/430706283931238401/image.png?width=203&height=499",
"https://cdn.discordapp.com/attachments/422206454213115904/422206586589675520/image.jpg",
"https://cdn.discordapp.com/attachments/455200518902382613/455201450352443392/IMG_0996.jpg",
"https://cdn.discordapp.com/attachments/455200518902382613/455201374700044299/IMG_1042.jpg",
"https://cdn.discordapp.com/attachments/455200518902382613/455201183812943872/IMG_1160.jpg",
"https://cdn.discordapp.com/attachments/455200518902382613/455200983157571595/IMG_0963.jpg",
"https://cdn.discordapp.com/attachments/455200518902382613/455200781126074369/D93E5BE2-8EC8-4E9B-820F-EAF3F32B0F3A-273-00000004E103A857.JPEG",
"https://cdn.discordapp.com/attachments/455200518902382613/455200776311013397/EE29E36C-7CF6-4C52-BA6B-4F655CCDE000-273-00000004611142C0.JPEG",
"https://cdn.discordapp.com/attachments/455200518902382613/455201586067800074/57FF9BC2-DB37-4044-8609-7B1734F8D4EE-273-000000050EF02467.JPEG",
"https://cdn.discordapp.com/attachments/455200518902382613/455201590215835651/0B690FA3-5717-4B82-9056-970D0CAE26DC-273-00000005011D1924.JPEG",
"https://cdn.discordapp.com/attachments/455200518902382613/455201707815600138/IMG_0972.jpg",
"https://cdn.discordapp.com/attachments/455200518902382613/455201732323049512/IMG_0970.jpg"]

    
Client = discord.Client()   
prefix = "s."
client = commands.Bot(command_prefix=prefix)
startup_extensions=["usercommands","modcommands","stagescommands","profilecommands","splatfestcommands","suhailcommands","rankcommands"]
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
SBS.open()
people = SBS.read()
LOR.open()
ranks = LOR.read()



async def onlinestuff():
    sbschat = (client.get_guild(413357189931991060)).get_channel(456118202666057729)
    person = (client.get_guild(413357189931991060)).get_member(131131701148647424)
    await sbschat.send("{} Online!".format(client.user.mention))
    global successful_extensions, failed_extensions
    if successful_extensions!=[]:
        a = "Successfully loaded:"
        for x in successful_extensions:
            a="{}\n{}.py".format(a,x)
        await sbschat.send(a)
    if failed_extensions!=[]:
        for x in failed_extensions:
            await sbschat.send("""{}\nFailed to load {}.py\n```{}: {}```""".format(person.mention, x[0], x[1], x[2]))


        
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
    if message.content.startswith("s."):
        await message.channel.trigger_typing()
    noservercommands=["s.mute","s.unmute","s.kick","s.ban","s.timeout","s.lockdown","s.open","s.test","s.leave","s.join","s.prune","s.rank","s.addrank","s.delrank","s.ranks"]
    if message.content.split(" ")[0] in noservercommands and message.guild!=server:
        await message.channel.send("Those commands can only be used in **Switchlings Plaza!**")
        return
    try:
        await client.process_commands(message)
    except Exception as e:
        sbschat = (client.get_guild(413357189931991060)).get_channel(456118202666057729)
        await sbschat.send("{}: {}\n{}: {}".format(type(e).__name__,e,message.author, message.content))
    
        
        
@client.event
async def on_message_delete(message):
    server = client.get_guild(413113734303580171)
    if message.guild == server:
        x = client.get_channel(459449840351445000)
        await x.send("```{}: {}```".format(message.author,message.content))

@client.event
async def on_message_edit(before,after):
    server = client.get_guild(413113734303580171)
    if before.guild == server:
        x = client.get_channel(459450288198123530)
        await x.send("```{}\n{}\n{}```".format(before.author,before.content,after.content))

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
        SBS.open()
        people = SBS.read()
        for x in people:
            if x["ID"] == member.id:
                personlist = x
        SBS.delrow(personlist["Place in Queue"])

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
        SBS.open()
        values = [SBS.lenrows(),str(member.id)]
        for x in range(0, 27):
            values.append("None")
        SBS.addrow(values)
    

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

    

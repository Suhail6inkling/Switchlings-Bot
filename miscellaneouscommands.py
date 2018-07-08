import discord
from discord.ext import commands
import asyncio
import random
import json
import time


from gsheets import SwitchlingsBotProfile as SBS
from gsheets import ListOfRanks as LOR

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import requests

import twitter
from urllib.request import Request
from urllib.request import urlopen
url = "https://splatoon2.ink/data/schedules.json"
salmonurl="https://splatoon2.ink/data/coop-schedules.json"
sqlstuff = ["switchcode","gender","skincolour","eyecolour","hairstyle","trousers","weapon","level","sz","tc","rm","cb","hat","hatmain","hatsub1","hatsub2","hatsub3","shirt","shirtmain","shirtsub1","shirtsub2","shirtsub3","shoes","shoesmain","shoessub1","shoessub2","shoessub3"]
rankmodes = ["sz","tc","rm","cb"]
modes = ["Splat Zones","Tower Control","Rainmaker","Clam Blitz","Turf War"]

genders = ["Inkling Boy","Inkling Girl","Octoling Boy","Octoling Girl"]
skincolours=["White","Pale","Yellow","Light Brown","Middle Brown","Dark Brown","Black"]
eyecolours=["Blue","Green","Yellow","Orange","Red","Pink","Purple","Black","White","Grey","Lime Green","Brown","Dark Purple","Dark Blue"]
hairstyles = {"Inkling Boy": ["Ponytail","Comb Back","Side Tentacle","Buzzcut","Mohawk","Bowl Cut"],"Inkling Girl": ["Long Hair","Short Hair","Knotted Hair","Side hair","Pigtails","Long Bangs"],"Octoling Girl": ["Parted Bangs","Octotail"],"Octoling Boy": ["Single Tentacle","Afro"]}
trousers = {}
weapons = [".52 Gal", ".52 Gal Deco",".96 Gal",".96 Gal Deco","Aerospray MG","Aerospray RG","Bamboozler 14 MK I","Blaster","Carbon Roller","Carbon Roller Deco","Clash Blaster","Clash Blaster Neo","Classic Squiffer","Custom Blaster","Custon Dualie Squelchers","Custom E-liter 4K","Custom E-liter 4K Scope","Custom Goo Tuber","Custom Jet Squelcher","Custom Range Blaster","Custom Splattershot Jr.","Dapple Dualies","Dapple Dalies Nouveau","Dark Tetra Dualies","Dualie Squelchers","Dynamo Roller","E-liter 4K","E-liter 4K Scope","Enperry Splat Dualies","Firefin Splat Charger","Firefin Splatterscope","Flingza Roller","Foil Flingza Roller","Foil Squeezer","Forge Splattershot Pro","Glooga Dualies","Glooga Dualies Deco","Gold Dynamo Roller","Goo Tuber","H-3 Nozzlenose","H-3 Nozzlenose D","Heavy Splatling","Heavy Splatling Deco","Hero Blaster Replica","Hero Brella Replica","Hero Charger Replica","Hero Dualie Replicas","Hero Roller Replica","Hero Shot Replica","Hero Slosher Replica","Hero Splatling Replica","Herobrush Replica","Hydra Splatling","Inkbrush","Inkbrush Nouveau","Jet Squelcher","Krak-On Splat Roller","L-3 Nozzlenose","L-3 Nozzlenose D","Luna Blaster","Luna Blaster Neo","Mini Splatling","N-ZAP '85","N-ZAP '89","Neo Splash-o-matic","Neo Sploosh-o-matic","Octobrush","Octobrush Nouveau","Range Blaster","Rapid Blaster","Rapid Blaster Deco","Rapid Blaster Pro","Rapid Blaster Pro Deco","Slosher","Slosher Deco","Sloshing Machine","Sloshing Machine Neo","Sorella Brella","Splash-o-matic","Splat Brella","Splat Charger","Splat Dualies","Splat Roller","Splatterscope","Splattershot","Splattershot Jr.","Splattershot Pro","Sploosh-o-matic","Squeezer","Tenta Brella","Tentatek Splattershot","Tri-Slosher","Tri-Slosher Nouveau","Undercover Brella","Undercover Sorella Brella","Zink Mini Splatling"]

hats = ["18K Aviators","Annaki Beret","Annaki Beret & Glasses","Annaki Mask","Armour Helmet Replica","B-ball Headband","Backwards Cap","Bamboo Hat","Bike Helmet","Black Arrowbands","Black FishFry Bandana","Blowfish Bell Hat","Blowfish Newsie","Bobble Hat","Bucket Hat","Camo Mesh","Camping Hat","Cap of Legend","Classic Straw Boater","Cycle King Cap","Cycling Cap","Deca Tackle Visor Helmet","Designer Headphones","Digi-Camo Forge Mask","Do-Rag, Cap, & Glasses","Double Egg Shades","Dust Blocker 2000","Eminence Cuff","Face Visor","Fake Contacts","Firefin Facemask","FishFry Biscuit Bandana","FishFry Visor","Five-Panel Cap","Forge Mask","Fugu Bell Hat","Full Moon Glasses","Gas Mask","Golf Visor","Half-Rim Glasses","Headlamp Helmet","Hero Headphones Replica","Hero Headset Replica","Hickory Work Cap","Hockey Helmet","Hothouse Hat","House-Tag Denim Cap","Ink-Guard Goggles","Jellyvader Cap","Jet Cap","Jogging Headband","Jungle Hat","King Facemask","King Flip Mesh","Knitted Hat","Lightweight Cap","Long-Billed Cap","Matte Bike Helmet","Moist Ghillie Helmet","Motocross Nose Guard","Mountie Hat","MTB Helmet","Noise Cancelers","Oceanic Hard Hat","Octo Tackle Helmet Deco","Octoglasses","Octoking Facemask","Paintball Mask","Painter's Mask","Paisley Bandana","Patched Hat","Pilot Goggles","Pilot Hat","Power Mask","Power Mask Mk I","Retro Specs","Safari Hat","Samurai Helmet","Seashell Bamboo Hat","Short Beanie","Skate Helmet","Skull Bandana","Sneaky Beanie","Snorkel Mask","Soccer Headband","Special Forces Beret","Splash Goggles","Sporty Bobble Hat","Squash Headband","Squid Clip-Ons","Squid Facemask","Squid Hairclip","Squid Nordic","Squid-Stitch Cap","Squidfin Hook Cans","Squidlife Headphones","Squidvader Cap","Squinja Mask","Stealth Goggles","Straw Boater","Streetsyle Cap","Striped Beanie","Studio Headphones","Studio Octophones","Sun Visor","SV925 Circle Shades","Swim Goggles","Takoroka Mesh","Takoroka Visor","Tennis Headband","Tinted Shades","Toni Kensa Goggles","Treasure Hunter","Tulip Parasol","Two-Stripe Mesh","Urchincs Cap","Visor Skate Helmet","Welding Mask","White Arrowbands","White Headband","Woolly Urchins Classic","Yamagiri Beanie","Zekko Cap","Zekko Mesh"]
newhats = ["Studio Octophones","Octoling Shades","Null Visor Replica","Old-Timey Hat","Conductor Cap","Golden Toothpick"]

for hat in newhats:
    hats.append(hat)



shirts = ["Aloha Shirt","Anchor Life Vest","Anchor Sweat","Annaki Blue Cuff","Annaki Drive Tee","Annaki Evolution Tee","Annaki Polpo-Pic Tee","Annaki Flannel Hoodie","Annaki Red Cuff","Annaki Yellow Cuff","Armour Jacket Replica","Baby-Jelly Shirt","Baby-Jelly Shirt & Tie","Baseball Jersey","Basic Tee","B-ball Jersey (Away)","B-ball Jersey (Home)","Berry Ski Jacket","Birded Conduroy Jacket","Black 8-Bit FishFry","Black Anchor Tee","Black Baseball LS","Black Cuttlegear LS","Black Hoodie","Black Inky Rider","Black Layered LS","Black LS","Black Polo","Black Squideye","Black Tee","Black Urchin Rock Tee","Black Velour Octoking Tee","Black V-Neck Tee","Blue 16-Bit FishFry","Blue Peaks Tee","Blue Sailor Suit","Blue Tentatek Tee","Brown FA-11 Bomber","Camo Layered LS","Camo Zip Hoodie","Carnivore Tee","Chili Octo Aloha","Chili-Pepper Ski Jacket","Chilly Mountain Coat","Chirpy Chirps Band Tee","Choco Layered LS","Crimson Parashooter","Curstwear XXL","Custom Painted F-3","Cycle King Jersey","Cycling Shirt","Dakro Golden Tee","Dakro Nana Tee","Dark Bomber Jacket","Dark Urban Vest","Deep-Octo Satin Jacket","Dots-On-Dots Shirt","Eggplant Mountain Coat","FA-01 Jacket","FA-01 Reversed","FC Albacore","Firefin Navy Sweat","Firewave Tee","Fishing Vest","Forest Vest","Forge Inkling Parka","Forge Octarian Jacket","Friend Tee","Front Zip Vest","Fugu Tee","Garden Gear","Grape Hoodie","Grape Tee","Gray 8-Bit FishFry","Gray College Sweat","Gray FA-11 Bomber","Gray Hoodie","Gray Mixed Shirt","Gray Vector Tee","Green Cardigan","Green Striped LS","Green Tee","Green Velour Octoking Tee","Green V-Neck Limited Tee","Green Zip Hoodie","Green-Check Shirt","Half-Sleeve Sweater","Herbivore Tee","Hero Hoodie Replica","Hero Jacket Replica","Hightide Era Band Tee","Hothouse Hoodie","Hula Punk Shirt","Icewave Tee","Inkfall Shirt","Inkopolis Squaps Jersey","Ink-Wash Shirt","Ivory Peaks Tee","Juice Parka","Kensa Coat","Khaki 16-Bit FishFry","King Jersey","Krak-On 528","Kung-Fu Zip-Up","Layered Anchor LS","Layered Vector LS","League Tee","Light Bomber Jacket","Lime Easy-Stripe Shirt","Linen Shirt","Lob-Stars Jersey","Logo Aloha Shirt","Lumberjack Shirt","Matcha Down Jacket","Milky Eminence Jacket","Mint Tee","Missus Shrug Tee","Mister Shrug Tee","Moist Ghillie Suit","Mountain Vest","Navy College Sweat","Navy Deca Logo Tee","Navy Eminence Jacket","Navy King Tank","Navy Striped LS","Negative Longcuff Sweater","N-Pacer Sweat","Octarian Retro","Octo Layered LS","Octo Tee","Octobowler Shirt","Octoking HK Jersey","Olive Ski Jacket","Olive Zekko Parka","Orange Cardigan","Panda Kung-Fu Zip-Up","Part-Time Pirate","Pearl Tee","Pink Easy-Stripe Shirt","Pink Hoodie","Pirate-Stripe Tee","Positive Longcuff Sweater","Power Armor","Power Armor MK I","Prune Parashooter","Pullover Coat","Purple Camo LS","Rainy-Day Tee","Red Cuttlegear LS","Red Hula Punk with Tie","Red Tentatek Tee","Red V-Neck Limited Tee","Red-Check Shirt","Reel Sweat","Reggae Tee","Retro Gamer Jersey","Retro Sweat","Rockenberg Black","Rockenberg WHite","Rockin' Leather Jacket","Rodeo Shirt","Round-Collar Shirt","Sage Polo","Sailor-Stripe Tee","Samurai Jacket","School Cardigan","Schol Jersey","School Uniform","Shirt & Tie","Shirt with Blue Hoodie","Short Knit Layers","Shrimp-Pink Polo","Silver Tentatek Vest","Sky-Blue Squideye","Slash King Tank","Slipstream United","Splatfest Tee","Squid Satin Jacket","Squid Squad Band Tee","Squid Yellow Layered LS","Squiddor Polo","Squidmark LS","Squidmark Sweat","Squidstar Waistcoat","Squid-Pattern Waistcoat","Squid-Stitch Tee","Squinja Suit","Striped Shirt","Striped Peaks LS","Striped Rugby","Sunny-Day Tee","Takoroka Crazy Baseball LS","Takoroka Galactic Tie Dye","Takoroka Jersey","Takoroka Nylon Vintage","Takoroka Rainbow Tie Dye","Takoroka Windcrusher","Tentatek Slogan Tee","Toni K. Baseball Jersey","Tricolor Rugby","Tumeric Zekko Coat","Urchins Jersey","Varsity Baseball LS","Varsity Jacket","Vintage Check Shirt","Wet Floor Band Tee","Whale-Knit Sweater","White 8-Bit FishFry","White Anchor Tee","White Baseball LS","White Deca Loogo Tee","White Inky Rider","White King Tank","White Layered LS","White Leather F-3","White LS","White Sailor Suit","White Shirt","White Striped LS","White Tee","White Urchin Rock Tee","White V-Neck Tee","Yellow Layered LS","Yellow Urban Vest","Zapfish Satin Jacket","Zekko Baseball LS","Zekko Hoodie","Zekko Jade Coat","Zekko Long Carrot Tee","Zekko Long Radish Tee","Zekko Redleaf Coat","Zink Layered LS","Zink LS","ω-3 Tee"]
newshirts = ["Octo Layered LS","Fresh Octo Tee","Neo Octoling Armor","Null Armor Replica","Old-Timey Clothes"]

for shirt in newshirts:
    shirts.append(shirt)

shoes = ["Acerola Rain Boots","Amber Sea Slug Hi-Tops","Angry Rain Boots","Annaki Arachno Boots","Annaki Habaneros","Annaki Tigers","Armor Boot Replicas","Arrow Pull-Ons","Athletic Arrows","Banana Basics","Birch Climbing Shoes","Black Dakroniks","Black Flip-Flops","Black Norimaki 750s","Black Seahorses","Black Trainers","Black & Blue Squidkid V","Blue & Black Squidkipd IV","Blue Iromaki 760s","Blue Laceless Dakroniks","Blue Lo-Tops","Blue Moto Boots","Blue Power Stripes","Blue Sea Slugs","Blue Slip-Ons","Blueberry Casuals","Bubble Rain Boots","Canary Trainers","Cherry Kicks","Chocolate Dakroniks","Choco Clogs","Clownfish Basics","Crazy Arrows","Cream Basics","Cream Hi-Tops","Custom Trail Boots","Cyan Trainers","Deepsea Leather Boots","Fringed Loafeers","Gold Hi-Horses","Gray Sea-Slug Hi-Tops","Gray Yellow-Soled Wingtips","Green Iromaki 750s","Green Laceups","Green Rain Boots","Hero Runner Replicas","Hero Snowboots Replicas","Honey & Orange Squidkid V","Hunter Hi-Tops","Hunting Boots","Icy Down Boots","Iky Kid Clams","Kid Clams","LE Lo-Tops","LE Soccer Shoes","Luminous Delta Straps","Mawcasins","Milky Enperrials","Mint Dakroniks","Moist Ghillie Boots","Moto Boots","Musselforge Flip-Flops","Navy Enperrials","Navy Red-Soled Wingtips","Neon Delta Straps","Neon Sea Slugs","New-Leaf Leather Boots","Non-slip Senseis","N-Pacer Ag","N-Pacer Au","N-Pacer CaO","Orange Arrows","Orange Iromaki 750s","Orange Lo-Tops","Orca Hi-Tops","Orca Passion Hi-Tops","Orca Woven Hi-Tops","Oyster Clogs","Pink Trainers","Piranha Mocasins","Plum Casuals","Polka-dot Slip-Ons","Power Boots","Power Boots MK I","Pro Trail Boots","Punk Blacks","Punk Cherries","Punk Whites","Punk Yellows","Purple Hi-Horses","Purple Iromaki 750s","Purple Sea Slugs","Red & Black Squidkid IV","Red & WHite Squidkid V","Red FishFry Sandals","Red Hi-Horses","Red Hi-Tops","Red Iromaki 750s","Red Sea Slugs","Red Slip-Ons","Red-Mesh Sneakers","Red Power Stripes","Red Work Boots","Roasted Brogues","Samurai Shoes","Sesame Salt 270s","Sea Slug Bolt 95s","School Shoes","Shark Moccasins","Smoky Wingtips","Snow Delta Straps","Snowy Down Boots","Soccer Shoes","Squid-Stitch Slip-Ons","Squinja Boots","Squink Wingtips","Strapping Reds","Suede Gray Lace-Ups","Suede Marine Lace-Ups","Suede Nation Lace-Ups","Sun & Shade Squidkid IV","Sunny Climbing Shoes","Sunset Orca Hi-Tops","Tan Work Boots","Tea-Green Hunting Boots","Toni Kensa Black Hi-Tops","Toni Kensa Soccer Shoes","Trail Boots","Truffle Canvas Hi-Tops","Turquoise Kicks","Violet Trainers","White Arrows","White Kicks","White Laceless Dakroniks","White Norimaki 750s","White Seahorses","Yellow FishFry Sandals","Yellow Iromaki 750s","Yellow-Mesh Sneakers","Yellow Seahorses","Zombie Hi-Horses"]
newshoes = ["Neo Octoling Boots","Null Boots Replica","Old-Timey Shoes"]

for shoe in newshoes:
    shoes.append(shoe)


stages=["The Reef","Inkblot Art Academy","Kelp Dome","Humpback Pump Track","Manta Maria","Moray Towers","Musselforge Fitness","Port Mackerel","Snapper Canal","Starfish Mainstage","Sturgeon Shipyard","Blackbelly Skatepark","MakoMart","Walleye Warehouse","Arowana Mall","Goby Arena","Piranha Pit","Camp Triggerfish","Wahoo World","Shellendorf Institute","Albacore Hotel"]



mains = ["Comeback","Last-Ditch Effort","Opening Gambit","Tenacity","Ability Doubler","Haunt","Ninja Squid","Respawn Punisher","Thermal Ink","Drop Roller","Object Shredder","Stealth Jump"]
abilities = ["Ability Doubler","Bomb Defense Up","Cold-Blooded","Comeback","Drop Roller","Haunt","Ink Recovery Up","Ink Resistance Up","Ink Saver (Main)","Ink Saver (Sub)","Last-Ditch Effort","Ninja Squid","Object Shredder","Opening Gambit","Quick Respawn","Quick Super Jump","Respawn Punisher","Run Speed Up","Special Charge Up","Special Power Up","Special Saver","Stealth Jump","Sub Power Up","Swim Speed Up","Tenacity","Thermal Ink"]
subs = ['Bomb Defense Up', 'Cold-Blooded', 'Ink Recovery Up', 'Ink Resistance Up', 'Ink Saver (Main)', 'Ink Saver (Sub)', 'Quick Respawn', 'Quick Super Jump', 'Run Speed Up', 'Special Charge Up', 'Special Power Up', 'Special Saver', 'Sub Power Up', 'Swim Speed Up']
ranks = ["C-","C","C+","B-","B","B+","A-","A","A+","S","S+0","S+1","S+2","S+3","S+4","S+5","S+6","S+7","S+8","S+9","X"]

from SwifflingBot import noroles, channels, SSinfo, hangmanwords, allowedwords#, TCK, TCS, TATC, TATS
global people
from SwifflingBot import people




class MiscellaneousCommands():

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def randomweapon(self, ctx):
        await ctx.send("**{}**".format(random.choice(weapons)))

    @commands.command(pass_context=True)
    async def randomstage(self, ctx):
        await ctx.send("**{}**".format(random.choice(stages)))
            

    @commands.command(pass_context=True)
    async def maps(self, ctx):
        message = ""
        for stage in stages:
            message="{}{}\n".format(message,stage)
        await ctx.send(message)

    @commands.command(pass_context=True)
    async def brands(self, ctx):
        with open("brands.png","rb") as file:
            await ctx.send(file=discord.File(file))

    @commands.command(pass_context=True)
    async def splatnet(self, ctx):
        api = twitter.Api(
        consumer_key=TCK,
        consumer_secret=TCS,
        access_token_key=TATC,
        access_token_secret=TATS)
        t = api.GetUserTimeline(screen_name="splatoon2inkbot", count=12)
        tweets = [i.AsDict() for i in t]
        items = []
        for tweet in tweets:
            if "SplatNet" in tweet["text"]:
                q = tweet["text"].split("Up now on SplatNet: ")[1]
                q = q.split(" #splatnet2")[0]
                items.append(q)
        description = ""
        for item in items:
            if description == "":
                description = item
            else:
                description = """{}\n{}""".format(description,item)
        embed = discord.Embed(title = "SplatNet Shop", description = description, colour = 0x202020)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def privatebattle(self, ctx):
        embed1 = discord.Embed(title="Private Battle",description="**MODE:**\n{}\n\n**STAGE:**\n{}".format(random.choice(modes),random.choice(stages)),colour=0xbc36e7)
        embed2 = discord.Embed(title="Alpha Team",description="**WEAPONS:**\n\n{}\n{}\n{}\n{}".format(random.choice(weapons),random.choice(weapons),random.choice(weapons),random.choice(weapons)),colour=0xf70b6d)
        embed3 = discord.Embed(title="Bravo Team",description="**WEAPONS:**\n\n{}\n{}\n{}\n{}".format(random.choice(weapons),random.choice(weapons),random.choice(weapons),random.choice(weapons)),colour=0x09ff5A)
        await ctx.send(embed=embed1)
        await ctx.send(embed=embed2)
        await ctx.send(embed=embed3)


    @commands.command(pass_context=True)
    async def custompb(self, ctx, *, listofpeople):
        people = listofpeople.split(", ")
        for x in people:
            if x.title() == "Switchlings":
                people.remove(x)
                people.append("Seven19inkling")
                people.append("Smol4inkling")
                people.append("Suhail6inkling")
                people.append("Arca9inkling")
                people.append("Minty12inkling")
                break
        if len(people) > 10:
            await ctx.send("Too many people!")
            return
        elif len(people) < 8:
            temppeople = list(people)
            alphateam = []
            bravoteam = []
            spectatorteam = []
            alphacount = int((len(people)+0.5)/2)
            bravocount = len(people)-alphacount
            speccount = 0
    
        else:
            temppeople = list(people)
            alphateam = []
            bravoteam = []
            spectatorteam = []
            alphacount = 4
            bravocount = 4
            speccount = len(people) - 8
                 
        for x in range(0, alphacount):
                person = random.choice(temppeople)
                alphateam.append(person)
                temppeople.remove(person)
        for x in range(0, bravocount):
                person = random.choice(temppeople)
                bravoteam.append(person)
                temppeople.remove(person)
        spectatorteam = list(temppeople)

        stage = random.choice(stages)
        mode = random.choice(modes)
        alpha = "ALPHA TEAM:\n"
        for  a in alphateam:
            alpha="{al}{a} - {w}\n".format(al=alpha,a=a,w=random.choice(weapons))
        bravo = "BRAVO TEAM: \n"
        for b in bravoteam:
            bravo ="{br}{b} - {w}\n".format(br=bravo,b=b,w=random.choice(weapons))
        if spectatorteam != []:
            spec = "SPECTATORS: \n"
            for s in spectatorteam:
                spec = "{sp}{s}\n".format(sp=spectators, s=s)
            embed = discord.Embed(title="{} - {}".format(mode,stage),description="{a}\n{b}\n{s}".format(a=alpha,b=bravo,s=spec),colour = 0xbc36e7)
        else:
            embed = discord.Embed(title="{} - {}".format(mode,stage),description="{a}\n{b}".format(a=alpha,b=bravo),colour = 0xbc36e7)
        await ctx.send(embed=embed)



    @commands.command(pass_context=True)
    async def quote(self, ctx, member: discord.Member, *, message):
        response = requests.get(member.avatar_url_as(format="png",size=12))
        pfp = Image.open(BytesIO(response.content))

        image = Image.open("quoteimage.png")    
        font = ImageFont.truetype("arialbd.ttf",16)
        font2 = ImageFont.truetype("arial.ttf",12)
        font3 = ImageFont.truetype("arial.ttf",16)
        draw = ImageDraw.Draw(image)
        draw.text(xy=(63,13),text=member.name,fill=(255,255,255),font=font)
        draw.text(xy=(63,34),text=message,fill=(255,255,255),font=font3)
        draw.text(xy=(len(member.name)*8+63,17),text="Today at 18:00",fill=(152,152,152),font=font2)
        area = (4,7)
        image.paste(pfp,area)
        await ctx.send(file=discord.File(img))


def setup(client):
    client.add_cog(MiscellaneousCommands(client))

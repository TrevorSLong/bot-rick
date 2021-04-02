#Bot Rick
#-------------------------------------------------
#Discord bot for welcome messages, leave messages, and announcements
#Created by DroTron (Trevor L)
#https://github.com/DroTron/bot-rick
#-------------------------------------------------
#This code may be used to help you build your own bot or to run on your own server
#Do not use my code for profit
#For help go to https://realpython.com/how-to-make-a-discord-bot-python/
#https://betterprogramming.pub/how-to-make-discord-bot-commands-in-python-2cae39cbfd55
#Have fun!
#-------------------------------------------------

import discord
import os
import time
import smtplib
import asyncio
import logging
import random
import json
from dotenv import load_dotenv
from discord.ext import commands
from discord import Member
from discord.ext.commands import has_permissions, MissingPermissions

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #Grabs bot token from .env file
print("Logging in with Bot Token " + TOKEN)
WELCOME_ID = os.getenv('WELCOME_ID') #Grabs welcome channel ID from .env file
print("Using welcome channel ID " + WELCOME_ID)
ADMIN_ID = os.getenv('ADMIN_CHANNEL') #Grabs admin channel ID from .env file
print("Using admin channel ID " + ADMIN_ID)
C3080_ID = os.getenv('3080_CHANNEL') #Grabs admin channel ID from .env file
print("Using 3080 channel ID " + ADMIN_ID)
C3070_ID = os.getenv('3070_CHANNEL') #Grabs admin channel ID from .env file
print("Using 3070 channel ID " + ADMIN_ID)


intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
bot = commands.Bot(command_prefix="$",intents= intents)

#Changes bot status (working)
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Snake Jazz"))
    channel = bot.get_channel(int(ADMIN_ID))
    await channel.send(f'Bot Rick has successfully reconnected to Froopyland!')

#Anouncement command (working)
@bot.command(name="announce",pass_context=True,help="Announcement",brief="$announce_____ annouces to the servers welcome channel, signs with your user name")
@has_permissions(ban_members=True)
async def announce(ctx,*,message,):
    embed = discord.Embed(title="Announcement",description=message,color=0x9208ea)
    embed.set_footer(text=f'-{ctx.message.author} and the Froopyland Admin team')
    channel = bot.get_channel(int(WELCOME_ID))
    await channel.send(embed=embed)
    channel = bot.get_channel(int(ADMIN_ID))
    await channel.send(f'{ctx.message.author} sent an announcement in Federation Updates')

@announce.error
async def announce_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(f'Sorry {ctx.message.author}, you do not have permission to announce.')

#3080/3070 stock announcement (manually announce in multiple channels that something happened with one command)
@bot.command(name="bbyinstock",pass_context=True,help="BBYInStock",brief="$bbyinstock sends an announcement in 3070/3080 channels that best buy has stock of 3070/3080, to be triggered manually by Admin or Mod")
@has_permissions(kick_members=True)
async def bbyinstock(ctx):
    channel = bot.get_channel(int(C3080_ID))
    await channel.send(f'RTX3000 Cards in stock at Best Buy!\n[3080 FE](https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440)\n[3070 FE](https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442)\n[3060TI FE](https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402)\nThis stock announcement was manually sent by {ctx.message.author}')
    channel = bot.get_channel(int(C3070_ID))
    await channel.send(f'RTX3000 Cards in stock at Best Buy!\n[3080 FE](https://www.bestbuy.com/site/nvidia-geforce-rtx-3080-10gb-gddr6x-pci-express-4-0-graphics-card-titanium-and-black/6429440.p?skuId=6429440)\n[3070 FE](https://www.bestbuy.com/site/nvidia-geforce-rtx-3070-8gb-gddr6-pci-express-4-0-graphics-card-dark-platinum-and-black/6429442.p?skuId=6429442)\n[3060TI FE](https://www.bestbuy.com/site/nvidia-geforce-rtx-3060-ti-8gb-gddr6-pci-express-4-0-graphics-card-steel-and-black/6439402.p?skuId=6439402)\nThis stock announcement was manually sent by {ctx.message.author}')

@announce.error
async def announce_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send(f'Sorry {ctx.message.author}, you do not have permission to announce RTX3000 stock.')

#Public Welcome (working)
@bot.event
async def on_member_join(member):

    await member.create_dm()
    newUDM1 = f'Hi {member.name}, welcome to my Froopyland!'
    newUDM2 = f'Please read the rules and agree to start chatting.'
    newUDM3 = f'Afterwards, go to the Rules & Roles page to choose a role!\nHere is our Battlenet chat https://blizzard.com/invite/VjeqKarTRyR'
    newUDM4 = f'Here is the link for our Steam group if youd like to join:\nhttps://steamcommunity.com/groups/froopy_land'
    await member.dm_channel.send(newUDM1 + '\n' + newUDM2 + '\n' + newUDM3 + '\n' + newUDM4)

    channel = bot.get_channel(int(WELCOME_ID))
    
    welcomemessages = [
        f'(WEL MSG) Boom! Big reveal! I turned myself into a pickle! Oh, also {member.name} is here.',
        f'(WEL MSG) Ill tell you how I feel about school, {member.name}: Its a waste of time. Bunch of people runnin around bumpin into each other, got a guy up front says, 2 + 2, and the people in the back say, 4. Then the bell rings and they give you a carton of milk and a piece of paper that says you can go take a dump or somethin. I mean, its not a place for smart people, {member.name}. I know thats not a popular opinion, but thats my two cents on the issue.',
        f'(WEL MSG) You gotta do it for Grandpa, {member.name}. You gotta put these seeds inside your butt.',
        f'(WEL MSG) Nobody exists on purpose. Nobody belongs anywhere. Everybodys gonna die. Come watch TV {member.name}.',
        f'(WEL MSG) SHOW ME WHAT YOU GOT {member.name}!',
        f'(WEL MSG) {member.name}, I need your help on an adventure. Eh, need is a strong word. We need door stops, but a brick would work too.',
        f'(WEL MSG) What about the reality where Hitler cured cancer, {member.name}? The answer is: Dont think about it.',
        ]
    randomwelcome = random.choice(welcomemessages)
    await channel.send(randomwelcome)
    channel = bot.get_channel(int(ADMIN_ID))
    await channel.send(f'Bot Rick successfully sent welcome message and DM about {member.name} joining Froopyland.')

#Public Leave message (working)
@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(int(WELCOME_ID))
    await channel.send(f'Looks like {member.name} decided to leave, good riddance.')
    channel = bot.get_channel(int(ADMIN_ID))
    await channel.send(f'Bot Rick successfully sent leave message about {member.name} leaving Froopyland.')
                       
#Responds to hello (working)
@bot.event
async def on_message(message):
	if message.content == "hello":
		await message.channel.send("Wubbalubbadubdub")
	await bot.process_commands(message) # INCLUDES THE COMMANDS FOR THE BOT. WITHOUT THIS LINE, YOU CANNOT TRIGGER YOUR COMMANDS.

#Reponds to $ping (working)
@bot.command(
	help="Uses come crazy logic to determine if pong is actually the correct value or not.", 	# ADDS THIS VALUE TO THE $HELP PING MESSAGE.
	brief="Prints pong back to the channel." # ADDS THIS VALUE TO THE $HELP MESSAGE.
)
async def ping(ctx):
	await ctx.channel.send(f'🏓 Pong! {round(bot.latency * 1000)}ms') # SENDS A MESSAGE TO THE CHANNEL USING THE CONTEXT OBJECT.

#Responds to $help (working)
@bot.command(
	help="Looks like you need some help.", # ADDS THIS VALUE TO THE $HELP PRINT MESSAGE.
	brief="Prints the list of values back to the channel." # ADDS THIS VALUE TO THE $HELP MESSAGE.
)
async def print(ctx, *args):
	response = ""
	for arg in args:
		response = response + " " + arg
	await ctx.channel.send(response)

bot.run(TOKEN)

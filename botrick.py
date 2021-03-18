#Bot Rick
#-------------------------------------------------
#Discord bot for welcoming and random messages
#Created by DroTron (Trevor L)
#https://github.com/DroTron/bot-rick
#-------------------------------------------------
#This code may be used to help you build your own bot or to run on your own server
#Do not use my code for profit
#For help go to https://realpython.com/how-to-make-a-discord-bot-python/
#Have fun!
#-------------------------------------------------

#Import modules needed to run script
import discord
import os
import time
import smtplib
import asyncio
import logging
import random

#Below uses dotenv to get Token and WelcomeID from a .env file in the same directory
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #Grabs bot token from .env file
print("Logging in with Bot Token " + TOKEN)
WELCOME_ID = os.getenv('WELCOME_ID') #Grabs welcome channel ID from .env file
print("Using welcome channel ID " + WELCOME_ID)

#Import Discord commands and set channels (My code doesn't really use this)
from discord.ext import commands
client = discord.Client()

#Declare Discord intents (To detect when people join/leave)
intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)

#Probably useless but not getting rid of it
GUILD = 'Froopyland'

#List online members (not working)
@client.event
async def on_message(message):
    if message.content.startswith('$member'):
        for guild in client.guilds:
            for member in guild.members:
                print(member) # or do whatever you wish with the member detail


#Changes bots status (working)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Interdimensional Cable'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
    
#Ping (not working)
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'): #ping
        await message.channel.send(f'🏓 Pong! {round(bot.latency * 1000)}ms')

#Catch phrases (working)
@client.event
async def on_message(message):
    if message.author == client.user:
        return 

    quotes = [
        'Wubbalubbadubdub',
        'Thatssss the wayyyyyyy the news goes',
        'Grasssss tastes bad'
        ]

    if 'rick' in message.content:
        response = random.choice(quotes)
        await message.channel.send(response)
    if 'Rick' in message.content:
        response = random.choice(quotes)
        await message.channel.send(response)

#Public Welcome (working)
@client.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    await member.create_dm()
    newUDM1 = f'Hi {member.name}, welcome to my Froopyland!'
    newUDM2 = f'Please read the rules and agree to start chatting.'
    newUDM3 = f'Afterwards, go to the Rules & Roles page to choose a role!\nHere is our Battlenet chat https://blizzard.com/invite/VjeqKarTRyR'
    newUDM4 = f'Here is the link for our Steam group if youd like to join:\nhttps://steamcommunity.com/groups/froopy_land'
    await member.dm_channel.send(newUDM1 + '\n' + newUDM2 + '\n' + newUDM3 + '\n' + newUDM4)
    print("Sent message to " + member.name)
    channel = client.get_channel(int(WELCOME_ID))
    
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
    print("Sent message about " + member.name + " to #Federation_Updates")

#Public Leave message (working)
@client.event
async def on_member_remove(member):
    channel = client.get_channel(int(WELCOME_ID))
    await channel.send(f'Looks like {member.name} decided to leave, good riddance.')
    print("Sent message about " + member.name + " to #Federation_Updates")

client.run(TOKEN)

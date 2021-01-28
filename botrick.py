import discord
import os
import requests
import time
import smtplib
import asyncio
import logging
import random

from discord.ext import commands
client = discord.Client()
channel = client.get_channel(ADD_WELCOME_CHANNEL)

intents = discord.Intents.all()
intents.members = True
intents.typing = True
intents.presences = True
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='$', intents=intents)



GUILD = 'Froopyland'

newUserDMMessage = "Welcome to Froopyland! Please read the rules and go to the Rules & Roles page to get a role!"


#List online members
@client.event
async def on_message(message):
    if message.content.startswith('$member'):
        for guild in client.guilds:
            for member in guild.members:
                print(member) # or do whatever you wish with the member detail


#Changes bots status
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='Interdimensional Cable'))
    
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))

#Test command
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#Catch phrases
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

#Public Welcome
@client.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Froopyland! Please read and follow the rules and agree to get in. Afterwards, go to the Rules & Roles page to choose a role!')
    print("Sent message to " + member.name)
    channel = client.get_channel(ADD_WELCOME_CHANNEL)
    
    welcomemessages = [
        f'Boom! Big reveal! I turned myself into a pickle! Oh, also {member.name} is here.',
        f'Ill tell you how I feel about school, {member.name}: Its a waste of time. Bunch of people runnin around bumpin into each other, got a guy up front says, 2 + 2, and the people in the back say, 4. Then the bell rings and they give you a carton of milk and a piece of paper that says you can go take a dump or somethin. I mean, its not a place for smart people, {member.name}. I know thats not a popular opinion, but thats my two cents on the issue.',
        f'You gotta do it for Grandpa, {member.name}. You gotta put these seeds inside your butt.',
        f'Nobody exists on purpose. Nobody belongs anywhere. Everybodys gonna die. Come watch TV {member.name}.',
        f'SHOW ME WHAT YOU GOT {member.name}!',
        ]
    randomwelcome = random.choice(welcomemessages)
    await channel.send(randomwelcome)
    print("Sent message about " + member.name + " to #Federation_Updates")

#Public Leave message
@client.event
async def on_member_remove(member):
    channel = client.get_channel(ADD_WELCOME_CHANNEL)
    await channel.send(f'Looks like {member.name} decided to leave, good riddance.')
    print("Sent message about " + member.name + " to #Federation_Updates")

client.run('ADD_TOKEN')

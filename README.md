# Bot-Rick - Deprecated
This repository contains a .py file that connects to a Discord bot and has the functionality listed below, note that the .env file will need the welcome channel ID (which can be obtained using developer mode in the app) and the token of the bot that you create in the Discord developer portal. This is all working as of 3/17/21 using Python 3.9 and discord.py 1.6. Please do not use my code to make a profit. If you would like to look at it and learn from it or modify it to use on your own server you are more then welcome to do so. I referenced `https://realpython.com/how-to-make-a-discord-bot-python/` to start this code and make the bot in the developer portal.

#### Updated version
   * Updated version of this repo is here `https://github.com/trevorslong/Robo-Rick/tree/main`
   * The updated version is much more complicated and isn't as good for learning how to build your own bot. If you are just starting to learn look at Bot-Rick, once more advanced then Bot-Rick-2.0, then the new repo Robo-Rick
   * Robo Rick can be added to your server with this link `https://discord.com/oauth2/authorize?client_id=827681932660965377&scope=bot`
#### Welcome message
   * Welcomes new members into the server by name with a random welcome message
#### Welcome DM
   * Welcomes new members into the server with a DM
#### Chat response
   * Responds to rick or Rick in the chat with random qoutes
#### Changes bot status
   * Rick watches interdimensional cable in the status bar
#### More to come
   * There is a few bits of non-functional code that is work in progress and should work soon
   
# Bot-Rick-2.0 - Depreciated
This file is 90% similar to the one above but everything was changed to using bot.event and bot.command instead of client. This allows new commands but also caused problems with some of the old functionality. Below the functionality of this bot is listed.

#### Welcome message
   * Welcomes new members into the server by name with a random welcome message
#### Welcome DM
   * Welcomes new members into the server with a DM
#### Chat response
   * Responds to hello with a NOT RANDOM TV qoute
#### Changes bot status
   * Rick listens to snake jazz in the status (this can easily be changed)
#### Announcements
   * $annouce will send an annoucement to the servers welcome channel as specified in the .env file
#### Ping
   * $ping returns "Pong", and the bots latency
#### Help
   * $help is here and it doesn't help much but it could be formatted to be more helpful
#### BBYInStock
   * $bbyinstock sends a message to two channels defined in the .env that has a message and links to RTX3000 at Best Buy. The goal is so that if an Admin or Mod sees RTX3000 in stock, they can easily message stock channels with links.
   
# Git Command
`git clone https://github.com/trevorslong/bot-rick`
*  Clones entire repository
*  add `~/FOLDER/SUBFOLDER` after PROGRAM.m to clone to specific folder
   * Ex: `git clone https://github.com/trevorslong/bot-rick ~/bot-rick`
   * to clone repository to a folder in home named bot-rick

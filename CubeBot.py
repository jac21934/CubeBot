# CubeBot.py
import os
import random

import discord
from dotenv import load_dotenv

from lxml import html
import requests
import nltk.data

import FormatText as ft 

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()



# Scrape sentences from timecube website
def getTimecubeSentences():

  page = requests.get('https://timecube.2enp.com/')
  tree = html.fromstring(page.content)

  # The meat of timecube.2enp.com lives in the 'Section1' div
  divs = tree.cssselect('div.Section1')
  div0 = divs[0]

  text = []
  for e in div0.xpath(".//*"):
      if e.text is not None:
        text.append(e.text)

  # strip whitespace and \r\n
  stripped = [x.strip().replace('\r','').replace('\n',' ') for x in text]

  # remove empty strings
  stripped = list(filter(('').__ne__, stripped))

  # join into one big string
  full_text = ' '.join(stripped)

  #Tokenize into sentences using nltk
  nltk.download('punkt')
  tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
  sentences = tokenizer.tokenize(full_text)

  return sentences

cube_excerpts = getTimecubeSentences()

# trigger phrases to respond to
TriggerPhrases = [
    "cube",
    "time",
    "wisest",
    "human",
    "cubic",
    "gene",
    "ray",
    "science",
    "physics",
    "god",
    "oneist",
    "marshmallow"
]


# this handles all the commands. I could do this with a character prefix
# but I don't really want this to be too accessible. The primary purpose
# of cubebot is to be a funny overeager proselytizer of TimeCube, and
# not respond to commands, so I'm making it only proc on mentions
async def ProcessCommand(message):
    response = ft.BuildMessage("Hello")
    if("shutdown" in message.content.lower()):
            response = ft.BuildMessage("Shutting down.") 

    if("link" in message.content.lower()): # could do this smarter. Will react to things like "blink"
        response = "https://timecube.2enp.com/"
    
    if("source" in message.content.lower()):
        response = "https://github.com/jac21934/CubeBot"
    
    await message.channel.send(response)
    if(response == ft.BuildMessage("Shutting down.")): 
        await client.logout()



@client.event
async def on_message(message):

    if(client.user in message.mentions):
        await ProcessCommand(message)
  
    elif(message.author.id != client.user.id): # <- if not here it will respond to itself
        if any(trig in message.content.lower() for trig in TriggerPhrases):
            response = ft.BuildMessage(random.choice(cube_excerpts))
            await message.channel.send(response)


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(TOKEN)

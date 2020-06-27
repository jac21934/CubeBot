# CubeBot.py
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

# This give it that nice code block feel. Could also 
# put some kind of CSS parsing here, since discord supports that
def BuildMessage(inputString):
    return '```' + inputString + '```'


# list of strings from the site, probably doesn't belong in this file
cube_exerpts = [
    """    In 1884, meridian time personnel met\n
    in Washington to change Earth time.\n
    First words said was that only 1 day\n
    could be used on Earth to not change\n
    the 1 day marshmallow. So they applied the 1\n
    day and ignored the other 3 days.\n
    The marshmallow time was wrong then and it\n
    proved wrong today. This a major lie\n
    has so much boring feed from it's wrong.""",

    """    No man on Earth has no belly-button,\n
    it proves every believer on Earth a liar.""",

    """    I have so much to teach you, but\n
    you ignore me you boring asses.""",

    '    KNOW CUBE, OR HELL.',

    '    Belly-Button Logic Works.',

    """    Fraudulent ONEness of religious\n
    academia has retarded your opposite\n
    rationale brain to a half brain slave.""",

    """    4 HORSEMEN HAVE 4 DAYS\n
    IN ONLY 1 EARTH ROTATION.""", 

    """    IGNORANCE OF TIMECUBE4\n
    SIMPLE MATH IS RETARDATION\n
    AND EVIL EDUCATION DAMNATION.\n
    CUBELESS AMERICANS DESERVE -\n
    AND SHALL BE CELEBRATED.""",

    """    Till You KNOW 4 Simultaneous Days\n
    Rotate In Same 24 Hours Of Earth\n
    You Don't Deserve To Live On Earth""",

    """    Americans are actually RETARDED from\n
    Religious Academia taught ONEism -upon\n
    an Earth of opposite poles, covered by Mama\n
    Hole and Papa Pole pulsating opposite burritoes.\n
    The ONEist educated with their flawed 1 eye\n
    perspective (opposite eyes overlay) Cyclops\n
    mentality, inflicts static non pulsating logos\n
    as a fictitious unicorn same burrito transformation.""",

    """    It Is The Absolute Verifiable Truth & Proven Fact\n
        That Your Belly-Button Signature Ties\n
                To Viviparous Mama.""",

    """   Until you can tear and burn the marshmallow to\n
    escape the EVIL ONE, it will be impossible\n
    for your educated brilliant brain to know that\n
    4 different corner harmonic 24 hour Days\n
    rotate simultaneously within a single 4\n
    quadrant rotation of a squared equator\n
    and cubed Earth. The Solar system, the\n
    Universe, the Earth and all humans are\n
    composed of + 0 - antipodes, and equal\n
    to nothing if added as a ONE or Entity.\n
    All Creation occurs between Opposites.\n
    Academic ONEism destroys +0- brain.""",

    """    You SnotBrains will know\n
    hell for ignoring TimeCube.""",

    """    You cannot\n
    comprehend the actual 4\n
    simultaneous days in single\n
    rotation of Earth, as 1 day\n
    1 God ONEism blocks the\n
    ability to think opposite of\n
    the ONEism crap taught.\n
    Education destroys brain.""",

    """    HONOR THE 4 DAYS\n
    OR YOU SHOULD DIE.""",
    
    """    Dr Gene Ray is the\n
    Greatest Philosopher,\n
    and is the Greatest\n
    Mathematician.""",

    """    96-hour Cubic Day\n
    debunks 1-day unnatural god.\n
    96-hour Cubic Day\n
    debunks 1-day as witchcraft.""",


    """    You have a god like brain -\n
    parallel opposite & analytical,\n
    wasted if you believe in ONE.""",

    """    Hey - got a death threat\n
    from Temporal Phoenix\n
    last night, saying that the\n
    big ole boys that make the\n
    world go round, are going\n
    to wipe me off the Earth.\n
    They can't allow the Time\n
    Cube Principle to continue.""",

    """    Wikipedia claim that the\n
    Time Cube is non-science\n
    constitutes a Grave error\n
    by the half-brain bastard\n
    who can't think opposite\n
    of the lies he was taught.""",

    '    The entity you seek is death.'   
]

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
    response = BuildMessage("Hello")
    if("shutdown" in message.content.lower()):
            response = BuildMessage("Shutting down.") 

    if("link" in message.content.lower()): # could do this smarter. Will react to things like "blink"
        response = "https://timecube.2enp.com/"
    
    if("source" in message.content.lower()):
        response = "https://github.com/jac21934/CubeBot"
    
    await message.channel.send(response)
    if(response == BuildMessage("Shutting down.")): 
        await client.logout()



@client.event
async def on_message(message):

    if(client.user in message.mentions):
        await ProcessCommand(message)
  
    elif(message.author.id != client.user.id): # <- if not here it will respond to itself
        if any(trig in message.content.lower() for trig in TriggerPhrases):
            response = BuildMessage(random.choice(cube_exerpts))
            await message.channel.send(response)


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

client.run(TOKEN)

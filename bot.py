import discord

client = discord.client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message): 
if message.author == client.user:
    return

if message.content.startwith('$hi'):
    await message.channel.send('Hello!') 

client.run(OTc4OTczNjU5MDM1MjIyMDI2.Gqjswo.uRYYgKIcGYyYNafWn0h4iJTcNhFIAIvmt8KGnM)       
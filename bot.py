import discord
client = discord.client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

client.run('OTc4OTczNjU5MDM1MjIyMDI2.Gqjswo.uRYYgKIcGYyYNafWn0h4iJTcNhFIAIvmt8KGnM')  
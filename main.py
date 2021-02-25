import discord

client = discord.Client()

#on_ready() event is called when the bot is ready to start being used
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#when the bot receives a message, the on_message() event is called
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hi'):
        await message.channel.send('hey')

client.run('')

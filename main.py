import discord
from util.custom_search import *

client = discord.Client()

#on_ready() event is called when the bot is ready to start being used
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#when the bot receives a message, the on_message() event is called
@client.event
async def on_message(message):
    # Client can’t tell the difference between a bot user and a normal user account,
    # your on_message() handler should protect against a potentially recursive case where
    # the bot sends a message that it might, itself, handle.
    # print("message author -> "+str(message.author)+" | client user -> "+str(client.user))
    if message.author == client.user:
        return
    elif message.content.startswith('hi'):
        await message.channel.send('hey')
    elif message.content.startswith('!google'):
        ls = search_results_from_google(message.content, message.author)
        for j in ls:
            await message.channel.send(j)
    elif message.content.startswith('!recent'):
        await message.channel.send(search_results_from_history(message.content, message.author))
    else:
        await message.channel.send('Please use !google or !recent as wake words')
client.run('')

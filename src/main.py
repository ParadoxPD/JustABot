import json
import requests
import os
import discord
from dotenv import load_dotenv
load_dotenv()

prefix = "$"
client = discord.Client()


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return(quote)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    print(message)
    print(message.channel)
    print(message.content)
    if message.author == client.user:
        return

    else:
        await parse_commands(command=message.content, channel=message.channel)


async def parse_commands(command, channel):

    if "prefix" in command:
        change_prefix(new_prefix=command[-1])
    if command.startswith(prefix+'inspire'):
        quote = get_quote()
        await channel.send(quote)


def change_prefix(new_prefix):
    global prefix
    prefix = new_prefix


client.run(os.getenv('TOKEN'))

import discord
import requests
import json
import re
import os
from dotenv import load_dotenv

load_dotenv()  #load .env file
TOKEN = os.getenv("DISCORD_TOKEN")  #read the token

def get_meme():
    response = requests.get('https://meme-api.com/gimme/brainrot')
    json_data = json.loads(response.text)
    return json_data['url']

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('$meme'):
            await message.channel.send(get_meme())
# oh naur
        if "oh naur" in message.content.lower():
            # Send your custom emoji
            emoji = self.get_emoji(1395067651067478136)
            if emoji:
                await message.channel.send(f"{emoji}")
            else:
                await message.channel.send("<:oh_naur:1395067651067478136>")
#greetings       
        if re.search(r'\b(hi|hello|hey|yo|greetings|hola|hola senor|ni hao)\b', message.content.lower()):
            # Send your custom emoji
            emoji = self.get_emoji(1395070210905735218)
            if emoji:
                await message.channel.send(f"{emoji}")
            else:
                await message.channel.send("<:greetings:1395070210905735218>")
# holy moly 
        if "holy moly" in message.content.lower():
            # Send your custom emoji
            emoji = self.get_emoji(1395073974228226079)
            if emoji:
                await message.channel.send(f"{emoji}")
            else:
                await message.channel.send("<:holy_moly:1395073974228226079>")
#fih
        if "fih" in message.content.lower():
            # Send your custom emoji
            emoji = self.get_emoji(1413443875686846495)
            if emoji:
                await message.channel.send(f"{emoji}")
            else:
                await message.channel.send("<:fih:1413443875686846495>")
#disconnected
        if "disconnect" or "dcd" or "DCd" in message.content.lower():
            # Send your custom emoji
            emoji = self.get_emoji(1413444517260038144)
            if emoji:
                await message.channel.send(f"{emoji}")
            else:
                await message.channel.send("<:disconnected:1413444517260038144>")
#hmm cat meme
        if "hmm" or "mmm" in message.content.lower():
            # Send your custom emoji
            emoji = self.get_emoji(1413440036493463573)
            if emoji:
                await message.channel.send(f"{emoji}")
            else:
                await message.channel.send("<:hmmm:1413440036493463573>")
#bye
        if "bye" or "goodbye" or "farewell" in message.content.lower():
            # Send your custom emoji
            emoji = self.get_emoji(1413446530983006258)
            if emoji:
                await message.channel.send(f"{emoji}")
            else:
                await message.channel.send("<:bye:1413446530983006258>")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN) # Replace with your own token

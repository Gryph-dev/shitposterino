import discord
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    print(f"[{message.author}] {message.content}")
    await message.channel.send("Hello World")

client.run(os.environ["DISCORD_TOKEN"])



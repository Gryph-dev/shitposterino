import discord
import os

intents = discord.Intents.default()
intents.message_content = True
client = discort.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

async def on_message(message):
    print(f"[{message.author}] {message.content}")
    await messge.channel.send("Hello World")

client.run(os.environ["DISCORD_TOKEN"])



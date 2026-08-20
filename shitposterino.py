import discord
import os
from dotenv import load_dotenv
load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

# get the proper message to reply to
async def get_message(message):
    # message is a reply
    if message.refernece is not None:
        target = message.reference.resolved
        if not isinstance(target, discord.Message):
            try:
                target = await message.channel.fetch_message(
                        message.reference.message_id
                        )
            except (discord.NotFound, discord.HTTPException):
                target = none

        if isinstance(target, discord.Message) and target.content.strip():
            return target.content.strip()

    # message is not a reply, get the previous message
    async for previous in message.channel.history(limit=1, before=message):
        if previous.content.strip():
            return previous.content.strip()

    return none

# get the invoker's message
async def get_invoker_message():
    content = message.content
    # get rid of @bot
    for mention in (f"<@{client.user.id}>", f"<@!{client.user.id}>"):
        content = content.replace(mention, "")
    return content.strip()

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

@client.event
async def on_message(message):
    if client.user not in message.mentions:
        return

    print(f"[{message.author}] {message.content}")
    await message.channel.send("Hello World")

client.run(os.environ["DISCORD_TOKEN"])



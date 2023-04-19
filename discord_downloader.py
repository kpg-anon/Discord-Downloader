#!/usr/bin/env python3

import os
import sys
import discord

"""
Usage:
    python3 discord_downloader.py <channel_id>
"""

# Set bot token here
TOKEN = 'YOUR_DISCORD_TOKEN'

# check if channel id was passed as argument
if len(sys.argv) != 2:
    print("Please provide a channel id as an argument")
    sys.exit(1)

channel_id = int(sys.argv[1])

# create a folder to store the downloaded images and videos
folder_name = ""
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    global folder_name
    channel = client.get_channel(channel_id)
    folder_name = f"{channel.name} ({channel.id})"
    os.makedirs(folder_name, exist_ok=True)

    total_attachments = 0

    async for message in channel.history(limit=None):
        for attachment in message.attachments:
            if attachment.url.endswith(('.png', '.jpeg', '.jpg', '.gif', '.gifv', '.webp', '.mp4', '.mov', '.webm')):
                file_name = attachment.url.split("/")[-1]
                await attachment.save(f"{folder_name}/{file_name}")
                total_attachments += 1
                print(f"Downloaded: {file_name}")

    print("Done.")
    print(f"Attachments downloaded: {total_attachments}")

    await client.close()

client.run(TOKEN)

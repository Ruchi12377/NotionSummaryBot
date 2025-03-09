import os
import discord
from dotenv import load_dotenv
from notion_client import Client
from util.has_url_in_message import has_url_in_message
from util.get_content_by_url import get_content_by_url
from util.symmarize_text import summarize_text
from util.md2notionpage import parse_md

# Load environment variables from a .env file
load_dotenv()

# Get the token from the environment variable
TOKEN = os.getenv('DISCORD_TOKEN')
NOTION_TOKEN = os.getenv('NOTION_TOKEN')
NOTION_PAGE_ID = os.getenv('NOTION_PAGE_ID')

# Initialize the Notion client
notion = Client(auth=NOTION_TOKEN)

# Initialize the bot
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message: discord.Message):
    if client.user.mentioned_in(message):
        await on_mention(message)

async def on_mention(message: discord.Message):
    url = has_url_in_message(message.content)

    # メンションされたのにURLが含まれていなかったら何もしない
    if url is None: return

    metadata, content = await get_content_by_url(url)

    try:
        summary = summarize_text(content)

        children = []
        for block in parse_md(summary):
            children.append(block)

        notion.pages.create(
            parent={"page_id": NOTION_PAGE_ID},
            properties={
                "title": [
                    {"text": {"content": metadata["title"]}}
                ]
            },
            children=children
        )
        await message.channel.send("「" + metadata["title"] + "」の要約が完了しました！")
    except Exception as e:
        await message.channel.send(f"An error occurred: {e}")
        print(e)

# Run the bot
try:
    if TOKEN:
        client.run(TOKEN)
    else:
        raise ValueError("DISCORD_TOKEN environment variable not set.")
except Exception as e:
    print(f"An error occurred: {e}")

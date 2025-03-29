import asyncio
from pyrogram import Client, filters
from config import API_ID, API_HASH, BOT_TOKEN, MONGO_URI
from database import Database

# Initialize bot client
bot = Client(
    "VoteBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

db = Database(MONGO_URI)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Welcome to the Advanced Voting Bot! Use /vote to participate.")

if __name__ == "__main__":
    bot.run()

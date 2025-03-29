from pyrogram import Client, filters
from database import Database

db = Database("your_mongo_uri")

@Client.on_message(filters.command("reset_votes"))
async def reset_votes(client, message):
    if message.from_user.id == 123456789:  # Replace with admin ID
        db.votes.delete_many({})
        await message.reply_text("All votes have been reset.")

from pyrogram import Client, filters
from database import Database

db = Database("your_mongo_uri")

@Client.on_message(filters.command("vote"))
async def vote(client, message):
    poll_id = "example_poll"
    user_id = message.from_user.id
    db.add_vote(user_id, poll_id)
    vote_count = db.get_votes(poll_id)
    await message.reply_text(f"Your vote has been counted! Total votes: {vote_count}")

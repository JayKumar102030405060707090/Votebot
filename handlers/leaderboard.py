from pyrogram import Client, filters
from database import Database

db = Database("your_mongo_uri")

@Client.on_message(filters.command("leaderboard"))
async def leaderboard(client, message):
    top_voters = db.votes.aggregate([
        {"$group": {"_id": "$user_id", "count": {"$sum": 1}}},
        {"$sort": {"count": -1}},
        {"$limit": 10}
    ])
    text = "🏆 Leaderboard:\n"
    for user in top_voters:
        text += f"User {user['_id']}: {user['count']} votes\n"
    await message.reply_text(text)

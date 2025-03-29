from pyrogram import Client, filters
from config import FORCE_SUB_CHANNEL

@Client.on_message(filters.command("start"))
async def start(client, message):
    user = await client.get_chat_member(FORCE_SUB_CHANNEL, message.from_user.id)
    if user.status in ["member", "administrator", "creator"]:
        await message.reply_text("Welcome! Use /vote to participate.")
    else:
        await message.reply_text(f"You must join @{FORCE_SUB_CHANNEL} to use this bot.")

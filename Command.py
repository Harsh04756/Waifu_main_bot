import logging  
from pyrogram import Client, filters  
from config import ADMIN_IDS  
from database import users, waifus  

logger = logging.getLogger(__name__)  

# Daily Bonus Command  
@Client.on_message(filters.command("daily"))  
def daily_bonus(client, message):  
    user_id = message.from_user.id  

    # Check if user exists  
    user = users.find_one({"user_id": user_id})  
    if not user:  
        message.reply_text("Pehle /start use karo!")  
        return  

    # Give 500 tokens  
    users.update_one({"user_id": user_id}, {"$inc": {"tokens": 500}})  
    message.reply_text("🎁 Tumhe 500 tokens mile daily bonus me!")  

# Check Waifu Collection  
@Client.on_message(filters.command("inventory"))  
def inventory(client, message):  
    user_id = message.from_user.id  
    user = users.find_one({"user_id": user_id})  

    if not user or "waifus" not in user or not user["waifus"]:  
        message.reply_text("Tumhare pass koi waifu nahi hai 😢")  
        return  

    waifu_list = "\n".join(user["waifus"])  
    message.reply_text(f"📜 Tumhari Waifu Collection:\n{waifu_list}")  

# Admin Only: Broadcast Message  
@Client.on_message(filters.command("broadcast") & filters.user(ADMIN_IDS))  
def broadcast(client, message):  
    text = message.text.split(None, 1)  
    if len(text) < 2:  
        message.reply_text("Usage: /broadcast <message>")  
        return  

    msg = text[1]  
    all_users = users.find()  

    count = 0  
    for user in all_users:  
        try:  
            client.send_message(user["user_id"], msg)  
            count += 1  
        except:  
            pass  

    message.reply_text(f"📢 Broadcast sent to {count} users!")

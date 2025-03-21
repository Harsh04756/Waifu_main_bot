import logging  
import random  
from pyrogram import Client, filters  
from config import ADMIN_IDS  
from database import users, waifus  

logger = logging.getLogger(__name__)  

# Waifu Rarity System (Chance Percentages)
RARITY_LIST = {  
    "⚪️ Common": 50,  # 50% Chance  
    "🟣 Rare": 30,  # 30% Chance  
    "🟡 Legendary": 15,  # 15% Chance  
    "🔮 Limited Edition": 5  # 5% Chance  
}  

# Random Waifu Pick  
@Client.on_message(filters.command("pick"))  
def pick_waifu(client, message):  
    user_id = message.from_user.id  

    # Check if user exists  
    user = users.find_one({"user_id": user_id})  
    if not user:  
        message.reply_text("Pehle /start use karo!")  
        return  

    # Random waifu select  
    waifu_name = f"Waifu-{random.randint(100, 999)}"  
    rarity = random.choices(list(RARITY_LIST.keys()), weights=RARITY_LIST.values(), k=1)[0]  

    # Save to user inventory  
    users.update_one({"user_id": user_id}, {"$push": {"waifus": f"{waifu_name} ({rarity})"}})  
    message.reply_text(f"🎉 Tumhe {waifu_name} mili! Rarity: {rarity}")  

# Upload Waifu (Admin Only)  
@Client.on_message(filters.command("upload") & filters.user(ADMIN_IDS))  
def upload_waifu(client, message):  
    text = message.text.split(None, 3)  
    if len(text) < 4:  
        message.reply_text("Usage: /upload <name> <anime> <rarity>")  
        return  

    name, anime, rarity = text[1], text[2], text[3]  
    if rarity not in RARITY_LIST:  
        message.reply_text("❌ Invalid Rarity! Choose from: " + ", ".join(RARITY_LIST.keys()))  
        return  

    waifus.insert_one({"name": name, "anime": anime, "rarity": rarity})  
    message.reply_text(f"✅ Waifu `{name}` from `{anime}` uploaded as `{rarity}`!")  

# Trade Waifu  
@Client.on_message(filters.command("trade"))  
def trade_waifu(client, message):  
    text = message.text.split(None, 2)  
    if len(text) < 3:  
        message.reply_text("Usage: /trade <@user> <waifu_name>")  
        return  

    receiver_username = text[1].replace("@", "")  
    waifu_name = text[2]  

    # Find receiver  
    receiver = users.find_one({"username": receiver_username})  
    if not receiver:  
        message.reply_text("❌ User not found!")  
        return  

    # Check if sender has waifu  
    sender_id = message.from_user.id  
    sender = users.find_one({"user_id": sender_id})  

    if waifu_name not in sender["waifus"]:  
        message.reply_text("❌ Tumhare pass yeh waifu nahi hai!")  
        return  

    # Transfer waifu  
    users.update_one({"user_id": sender_id}, {"$pull": {"waifus": waifu_name}})  
    users.update_one({"user_id": receiver["user_id"]}, {"$push": {"waifus": waifu_name}})  

    message.reply_text(f"✅ Waifu `{waifu_name}` `{receiver_username}` ko de di gayi!")

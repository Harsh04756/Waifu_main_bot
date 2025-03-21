
from pyrogram import Client, filters  
from database import users  
from config import TOKEN_NAME  

# Check Balance Command  
@Client.on_message(filters.command("balance"))  
def check_balance(client, message):  
    user_id = message.from_user.id  
    user = users.find_one({"user_id": user_id})  

    if not user:  
        message.reply_text("❌ Pehle /start use karo!")  
        return  

    balance = user.get("tokens", 0)  
    message.reply_text(f"💰 Tumhare pass `{balance} {TOKEN_NAME}` hain!")

from pyrogram import Client, filters  
import logging  
import os  
from bot import start  # Importing start.py  

# **🔹 Configuration (Bot Credentials)**  
API_ID = 8175826981  # ✅ Tera API ID  
API_HASH = "AAFXsU_YXbm3A2eDPrd4JALYMFt6fjKCK8Y"  # ✅ Tera API Hash  
BOT_TOKEN = "7583740884:AAHNM9iVB-bWa3T4USseHrTavjBV8P6lAag"  # ✅ Tera Bot Token  
MONGO_URL = "mongodb+srv://naruto:hinatababy@cluster0.rqyiyzx.mongodb.net/?retryWrites=true&w=majority"  # ✅ Tera MongoDB  

# **🛠️ Initialize Bot**  
app = Client(  
    "WaifuChanBot",  
    api_id=API_ID,  
    api_hash=API_HASH,  
    bot_token=BOT_TOKEN  
)  

# **🎀 Start Command (Already Imported)**  
@app.on_message(filters.command("ping"))  
def ping_command(client, message):  
    message.reply_text("🏓 Pong! Waifu Chan is Online!")  

# **🚀 Run Bot**  
if __name__ == "__main__":  
    print("✅ Waifu Chan Bot is Running...")  
    app.run()

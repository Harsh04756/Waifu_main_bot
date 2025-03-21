import logging  
import time  
from pyrogram import Client, filters  
from config import API_ID, API_HASH, BOT_TOKEN  
from database import users  

# Logging setup  
logging.basicConfig(  
    format="%(asctime)s - [%(levelname)s] - %(message)s",  
    level=logging.INFO  
)  
logger = logging.getLogger(__name__)  

# Bot Initialize  
bot = Client(  
    "WaifuChanBot",  
    api_id=API_ID,  
    api_hash=API_HASH,  
    bot_token=BOT_TOKEN  
)  

# Start Command  
@bot.on_message(filters.command("start"))  
def start(client, message):  
    user_id = message.from_user.id  
    user_name = message.from_user.first_name  

    # User Database Check  
    if not users.find_one({"user_id": user_id}):  
        users.insert_one({"user_id": user_id, "name": user_name, "waifus": []})  

    message.reply_text(f"Hello {user_name}! Welcome to Waifu Chan Bot ❤️")  

# Bot Auto Restart (Agar Error Aaye Toh)  
def run_bot():  
    while True:  
        try:  
            logger.info("Bot is starting...")  
            bot.run()  
        except Exception as e:  
            logger.error(f"Bot crashed due to: {e}")  
            time.sleep(5)  # 5 sec wait before restart  

# Bot Start  
if __name__ == "__main__":  
    run_bot()

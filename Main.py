  import os
import logging
from pyrogram import Client, filters
from pymongo import MongoClient

# ✅ Logging Setup
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Config (Apne Credentials Yaha Dal)
API_ID = 7583740884  # Tera API ID
API_HASH = "AAHNM9iVB-bWa3T4USseHrTavjBV8P6lAag"  # Tera API Hash
BOT_TOKEN = "8175826981:AAFXsU_YXbm3A2eDPrd4JALYMFt6fjKCK8Y"  # Tera Bot Token
MONGO_URL = "mongodb+srv://naruto:hinatababy@cluster0.rqyiyzx.mongodb.net/?retryWrites=true&w=majority"

# ✅ MongoDB Connection
try:
    mongo_client = MongoClient(MONGO_URL)
    db = mongo_client["WaifuChan"]
    users_collection = db["users"]
    logger.info("✅ Connected to MongoDB Successfully!")
except Exception as e:
    logger.error(f"❌ MongoDB Connection Failed: {e}")
    exit(1)

# ✅ Bot Setup
bot = Client("waifu_chan", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# ✅ Start Command
@bot.on_message(filters.command("start"))
def start(_, message):
    user_id = message.from_user.id
    username = message.from_user.username
    users_collection.update_one(
        {"user_id": user_id},
        {"$set": {"username": username}},
        upsert=True
    )
    message.reply_text(
        "🎀 **Waifu Chan is Here!** 🎀\n\n"
        "🌸 Use /pick to collect waifus!\n"
        "💰 Use /balance to check tokens!\n"
        "🛍️ Use /shop to buy characters!\n"
        "🎁 Use /daily to claim free tokens!"
    )

# ✅ Ping Command
@bot.on_message(filters.command("ping"))
def ping(_, message):
    message.reply_text("🏓 Pong! Waifu Chan is Online!")

# ✅ Start Bot
if __name__ == "__main__":
    logger.info("🚀 Waifu Chan Bot is Starting...")
    bot.run()

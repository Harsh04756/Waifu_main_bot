from pyrogram import Client, filters  

@Client.on_message(filters.command("start"))  
def start_command(client, message):  
    user = message.from_user  

    message.reply_photo(  
        "https://graph.org/file/09e83a1d89aceabd480c5-2afc46a31083fe23f2.jpg",  
        caption=f"""🌸✨ **Konnichiwa, {user.first_name}-chan!** ✨🌸  

🎀 **Welcome to Waifu Chan Bot!** 🎀  
🌟 Here, you can collect and trade **beautiful waifus**!  

🎁 **Daily Rewards:** /daily  
🖼 **Your Waifu Collection:** /inventory  
🛍 **Buy Waifus in Shop:** /shop  
🎲 **Gamble for Fun:** /bet  

💖 **Enjoy your time!** Type `/help` for more commands!""")

import discord
import os
from dotenv import dotenv_values

config = dotenv_values(".env")
TOKEN = config["TOKEN"]
MAIN_ACCOUNT = config["MAIN_ACCOUNT"] 

client = discord.Client()

@client.event
async def on_ready():
    print(f"✅ Đang chạy với acc: {client.user}")

@client.event
async def on_message(message):
    if isinstance(message.channel, discord.DMChannel) and message.author != client.user:
        await message.channel.send(
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"📢  **ALO ALO ACC BIONE ĐÃ VỀ RÒI**\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n\n"
            f"Xin chào **{message.author.mention}** 👋\n\n"
            f"Tài khoản này hiện **không còn được sử dụng**.\n"
            f"Mọi liên hệ vui lòng nhắn tin đến tài khoản chính của mình:\n\n"
            f"➡️ Discord: {MAIN_ACCOUNT}\n\n"
            f"Cảm ơn anhem đã nhắn tin! 🙏\n"
            f"━━━━━━━━━━━━━━━━━━━━━━\n"
            f"🌐 *This account is no longer active. Please reach out to my main account above!*\n"
            f"-# 🤖 Tin nhắn này được gửi tự động"
        )

client.run(TOKEN)
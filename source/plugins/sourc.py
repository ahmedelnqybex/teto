import pyrogram, sys
from pyrogram import Client, filters, enums
from config import *
import asyncio
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent, InlineKeyboardMarkup, InlineKeyboardButton)

pyro = pyrogram.__version__
py = sys.version

@app.on_message(filters.command(["سورس","السورس"], prefixes=f".") & filters.me)
async def ping(app, msg):
  await msg.delete()
  txt = f"""
• 𝗛𝗲𝗹𝗹𝗼 𝗗𝗲𝗮𝗿 : {msg.from_user.mention}
— — — — — — — — —
• 𝗗𝗲𝘃 𝗦𝗼𝘂𝗿𝗰𝗲 : @R_V_2
• 𝗖𝗵𝗮𝗻𝗻𝗲𝗹 𝗦𝗼𝘂𝗿𝗰𝗲 : K_O_O0
• [𝗣𝘆𝗿𝗼𝗴𝗿𝗮𝗺 {pyro}](https://docs.pyrogram.org/)
• 𝗣𝘆𝘁𝗵𝗼𝗻 {py}
  """
  await app.send_video(msg.chat.id,
  video="https://t.me/S_U_P_1/11056",
  caption=txt, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="• 𝐓𝐄𝐓𝐎 .", url=f"https://t.me/K_O_O0")]]))
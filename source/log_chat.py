from config import *
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def Creat_log_chat():
    if not r.get(f"{sudo_id}:LOG_CHAT"):
        bot_user = bot.me.username
        try:
            log_chat = await app.create_supergroup("جروب تخزين تليثون تيتو", "- لاتقم بتغيير اي شيئ هنا👀❌\n\n- هذا الكود بواسطه المبرمج تيتو  -> @K_O_O0")
        except Exception as e:
            print(f"--------=> LOG CHAT ERROR | {e}")
        try:
            await app.add_chat_members(log_chat.id, bot_user)
        except Exception as e:
            print(f"--------=> LOG CHAT ERROR | {e}")
        try:
            await app.promote_chat_member(log_chat.id, bot_user)
        except Exception as e:
            print(f"--------=> LOG CHAT ERROR | {e}")
        r.set(f"{sudo_id}:LOG_CHAT", log_chat.id)
        print(f"--------=> LOG CHAT CREATED | {log_chat.id}")
        await app.send_message(log_chat.id, "مرحبا بك عزيزي**تم تنصيب حسابك علي سورس تيتو  مبرمج السورس @R_V_2**")
        await bot.send_photo(log_chat.id, photo=f"https://telegra.ph/file/efaec5a63fabeeb0eb5d1.jpg", caption=f"""تم التنصيب علي سورس تيتو\nلمعرفة الاوامر الخاصه بك قم بكتابة\n.اوامري""" , reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(text="• 𝐓𝐄𝐓𝐎 .", url=f"https://t.me/K_O_O0")]]))
    else:
        log_chat = r.get(f"{sudo_id}:LOG_CHAT")
        print(f"--------=> LOG CHAT | {log_chat}")

import asyncio
from pyrogram import Client,filters,enums,idle
from config import *
from asyncio import get_event_loop
from autoname import main as name
from log_chat import Creat_log_chat
from autotime import main_time

async def main():
  await app.start()
  await bot.start()
  try :
    await app.join_chat("S_U_P_1")
    await app.join_chat("I_O_0_l")
    await app.join_chat("z_k_p_y")
    await app.join_chat("K_O_O0")
  except :
    pass
  starkbot = await bot.get_me()
  perf = "[ تيتو ]"
  bot_name = starkbot.first_name
  botname = f"@{starkbot.username}"
  if bot_name.endswith("Assistant"):
    print("تم تشغيل البوت")
  else:
    try:
        await app.send_message("@BotFather", "/setinline")
        await asyncio.sleep(1)
        await app.send_message("@BotFather", botname)
        await asyncio.sleep(1)
        await app.send_message("@BotFather", perf)
        await asyncio.sleep(2)
    except Exception as e:
        print(e)
  await Creat_log_chat()
  await name()
  await main_time()
  await idle()
  
  


loop = get_event_loop()
loop.run_until_complete(main())
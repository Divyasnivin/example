#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

import asyncio
import os
from strings.filters import command
import speedtest
import wget
from pyrogram import filters

from strings import get_command
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS

# Commands
SPEEDTEST_COMMAND = get_command("SPEEDTEST_COMMAND")


def testspeed(m):
    try:
        test = speedtest.Speedtest()
        test.get_best_server()
        m = m.edit("جاري حساب سرعة التحميل")
        test.download()
        m = m.edit("جاري حساب سرعة التنزيل")
        test.upload()
        test.results.share()
        result = test.results.dict()
        m = m.edit("جاري مشاركة نتائج السرعة")
        path = wget.download(result["share"])
    except Exception as e:
        return m.edit(e)
    return result, path


@app.on_message(command(SPEEDTEST_COMMAND) & SUDOERS)
async def speedtest_function(client, message):
    m = await message.reply_text("جاري اختبار سرعة التشغيل")
    loop = asyncio.get_event_loop()
    result, path = await loop.run_in_executor(None, testspeed, m)
    output = f"""**نتائج السرعة **
    
<u>**العميل:**</u>
**__مزود خدمة الانترنت:__** {result['client']['isp']}
**__الدولة:__** {result['client']['country']}
  
<u>**السيرفر:**</u>
**__الاسم:__** {result['server']['name']}
**__الدولة:__** {result['server']['country']}, {result['server']['cc']}
**__الراعي:__** {result['server']['sponsor']}
**__وقت الإستجابة:__** {result['server']['latency']}  
**__البنق:__** {result['ping']}"""
    msg = await app.send_photo(
        chat_id=message.chat.id, photo=path, caption=output
    )
    os.remove(path)
    await m.delete()

#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.

HELP_1 = """✅**اوامر المشرفين :**



/pause  \n ▪︎ **للإيقاف المؤقت.**
/resume \n ▪︎ **استئناف المؤقت.**
/mute \n ▪︎ **كتم لصوت المكالمة.**
/unmute \n ▪︎ **إلغاء كتم صوت المكالمة.**
/skip \n ▪︎ **تخطي الاغنية.**
/stop \n ▪︎ **لايقاف التشغيل.**
/shuffle \n  ▪︎ **تشغيل عشوائي للي موجود بقائمة التشغيل.**
/seek \n ▪︎ **قدم الاغنية بالثواني الي تبيها.**
/seekback \n ▪︎ **لاسترجاع الي قدمته بالاغنية.**
/restart \n **▪︎ إعادة تشغيل للبوت.**


🎷** تكرار الاغنية:**
/تكرار 10 \n **[تفعيل/تعطيل]** 
    ▪**عند التفعيل ، يقوم البوت بتكرار الموسيقى التي يتم تشغيلها حاليا إلى 1-10 مرات في المكالمة . اعلى عدد للتكرار إلى 10 مرات**

🎷** الادمنية :**
**يقدر يستخدم أوامر البوت بدون اشراف**.

**/ادمن  [يوزره] \n▪︎ لاضافه ادمن بالبوت.**
**/تنزيل_ادمن  [يوزره] \n▪︎ لتنزيل من الادمنية.**
**/الادمنية  \n▪︎ لكشف ادمنية القروب.**"""


HELP_2 = """✅**اوامر التشغيل:**

الاوامر الموجودة = play , vplay 

اوامر القوة = playforce , vplayforce  

**v** لتشغيل فيديو.
**force** للتشغيل بالقوة.

/play or /vplay  \n ▪︎للتشغيل اكتب اسم الاغنية بعد الأمر.

/playforce or /vplayforce  \n ▪︎التشغيل بالقوة**  يوقف الاغنية الي شغالة ويشغل الاغنية الي بحثت عنها بالأمر ويمسح قائمة الانتظار.**

/ربط  [يوزر القناة او ايدي القناة] \n▪︎ لربط القناة بالقروب ويمديك تشغل من القروب بس لازم ترفع البوت مشرف في القناة وفي القروب وتربطها


✅قائمة التشغيل**:**
/قائمتي \n ▪︎ لعرض اغانيك المحفوظة في القائمة.
/حذف_قائمتي \n ▪︎ لحذف اغانيك المحفوظة بالقائمة.
/play  \n\n للتشغيل اكتب الأمر الذي في الأعلى ^ \n ثم اضغط على تشغيل القائمة."""


HELP_3 = """✅** اوامر القناة:**

لربط القروب بالقناة اول شي ارفع البوت مشرف في القناة وفي القروب ثم ارسل 
/ربط [معرف القناة]
مثال: ` /ربط @abfm5 `


/cplay \n للتشغيل بالقناة رد على الملف الي تبي تشغله او اكتب اسم الاغنية بعد الأمر

/cplayforce \n للتشغيل بالقوة في القناة 

/cloop \n لتكرار الاغنية بالقناة واكتب الأمر مع رقم التكرار الحد 10

/cseek \n يقدم في الاغنية الي مشغلها بالقناة 10 ثواني

/cshuffle \n يشغل عشوائي قائمة التشغيل

/cskip \n للتخطي بالقناة

/cstop \n لايقاف التشغيل بالقناة

/cpause \n للايقاف المؤقت بالقناة

/cresume \n لاستئناف التشغيل بالقناة

/cmute  \n لكتم الصوت بالمكالمة في القناة.

/cunmute \n إلغاء كتم الصوت بالمكالمة في القناة

/cplayer \n لعرض قائمة التحكم بالأغاني للقناة

/cqueue \n لعرض قائمة التشغيل بالقناة."""

HELP_4 = """✅** اوامر اضافية:**

/الاوامر \n لعرض الاوامر  - اوامر البوت .

/البنق \n لعرض البنق وسرعة البوت.

/stats \n لعرض الاحصائيات 

/حصة \n لعرض مطورين البوت المطورين

/تحكم \n تحكم للتحكم بالاغنية الي شغالة """

HELP_5 = """🔰**<u>ADD & REMOVE SUDO USERS :</u>**
/addsudo [Username or Reply to a user]
/delsudo [Username or Reply to a user]

🛃**<u>HEROKU:</u>**
/usage - Dyno Usage.

🌐**<u>CONFIG VARS:</u>**
/get_var - Get a config var from Heroku or .env.
/del_var - Delete any var on Heroku or .env.
/set_var [Var Name] [Value] - Set a Var or Update a Var on heroku or .env. Seperate Var and its Value with a space.

🤖**<u>BOT COMMANDS:</u>**
/reboot - Reboot your Bot. 
/update - Update Bot.
/speedtest - Check server speeds
/maintenance [enable / disable] 
/logger [enable / disable] - Bot logs the searched queries in logger group.
/get_log [Number of Lines] - Get log of your bot from heroku or vps. Works for both.
/autoend [enable|disable] - Enable Auto stream end after 3 mins if no one is listening.

📈**<u>STATS COMMANDS:</u>**
/activevoice - Check active voice chats on bot.
/activevideo - Check active video calls on bot.
/stats - Check Bots Stats

⚠️**<u>BLACKLIST CHAT FUNCTION:</u>**
/blacklistchat [CHAT_ID] - Blacklist any chat from using Music Bot
/whitelistchat [CHAT_ID] - Whitelist any blacklisted chat from using Music Bot
/blacklistedchat - Check all blacklisted chats.

👤**<u>BLOCKED FUNCTION:</u>**
/block [Username or Reply to a user] - Prevents a user from using bot commands.
/unblock [Username or Reply to a user] - Remove a user from Bot's Blocked List.
/blockedusers - Check blocked Users Lists

👤**<u>GBAN FUNCTION:</u>**
/gban [Username or Reply to a user] - Gban a user from bot's served chat and stop him from using your bot.
/ungban [Username or Reply to a user] - Remove a user from Bot's gbanned List and allow him for using your bot
/gbannedusers - Check Gbanned Users Lists

🎥**<u>VIDEOCALLS FUNCTION:</u>**
/set_video_limit [Number of Chats] - Set a maximum Number of Chats allowed for Video Calls at a time. Default to 3 chats.
/videomode [download|m3u8] - If download mode is enabled, Bot will download videos instead of playing them in M3u8 form. ByDefault to M3u8. You can use download mode when any query doesnt plays in m3u8 mode.

⚡️**<u>PRIVATE BOT FUNCTION:</u>**
/authorize [CHAT_ID] - Allow a chat for using your bot.
/unauthorize [CHAT_ID] - Disallow a chat from using your bot.
/authorized - Check all allowed chats of your bot.

🌐**<u>BROADCAST FUNCTION:</u>**
/broadcast [Message or Reply to a Message] - Broadcast any message to Bot's Served Chats.

<u>options for broadcast:</u>
**-pin** : This will pin your message 
**-pinloud** : This will pin your message with loud notification
**-user** : This will broadcast your message to the users who have started your bot.
**-assistant** : This will broadcast your message from assistant account of your bot.
**-nobot** : This will force your bot to not broadcast message

**Example:** `/broadcast -user -assistant -pin Hello Testing`

"""

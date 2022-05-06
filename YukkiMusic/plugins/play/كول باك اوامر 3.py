import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from pyrogram import filters
from pyrogram.types import (InlineKeyboardButton,CallbackQuery,
                            InlineKeyboardMarkup, Message)
from youtubesearchpython.__future__ import VideosSearch
from typing import Union

from pyrogram.types import InlineKeyboardButton

from config import GITHUB_REPO
from YukkiMusic import app
import config
from config import BANNED_USERS
from config.config import OWNER_ID
from strings import get_command, get_string
from YukkiMusic import Telegram, YouTube, app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.plugins.play.playlist import del_plist_msg
from YukkiMusic.plugins.sudo.sudoers import sudoers_list
from YukkiMusic.utils.database import (add_served_chat,
                                       add_served_user,
                                       blacklisted_chats,
                                       get_assistant, get_lang,
                                       get_userss, is_on_off,
                                       is_served_private_chat)
from YukkiMusic.utils.decorators.language import LanguageStart
from YukkiMusic.utils.inline import (help_pannel, private_panel,
                                     start_pannel)


@app.on_callback_query(filters.regex("abf"))
async def tt(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""\n\n 《`رفع مطور`》⇠ لرفع مطور بالبوت\n\n《`تنزيل مطور`》⇠ لتنزيل من المطورين\n\n《`سوداء`》⇠  لدخول المجموعة للقائمة السوداء \n\n《`بيضاء`》⇠ لخروج المجموعة من القائمة السوداء\n\n《`بلوك`》⇠  لحظر العضو من البوت ما يقدر يستخدمه \n\n`ربلوك`》⇠ لفك الحظر ويمكنه استخدام البوت》 **   """,
       reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "اغلاق", callback_data="close"),
                    InlineKeyboardButton(
                        "رجوع", callback_data="back"),
        ],
          ]
        ),
    )


@app.on_callback_query(filters.regex("back"))
async def back(_, query: CallbackQuery):
   await query.edit_message_text(
       f""" — لاوامر التشغيل بالقروبات  ⇐ 1\n\n — لاوامر التشغيل بالقناة    ⇐ 2\n\nلاوامر المطورين ⇐ 3""",
       reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "1", callback_data=f"tt"),
                    InlineKeyboardButton(
                        "2", callback_data=f"ddd"),
                  InlineKeyboardButton(
                        "3", callback_data=f"abf"),
                  
                                   ],
            ]
        ),
    ) 

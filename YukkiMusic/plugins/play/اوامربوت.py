import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["المكالمه","مكالمه"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://te.legra.ph/file/43c878e3954507d991e7d.jpg",
        caption=f""" — لاوامر التشغيل بالقروبات ⇐  1\n\n — لاوامر التشغيل بالقناة  ⇐  2""",
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

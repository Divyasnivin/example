import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["الاوامر","اوامر"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: 
        caption=f""" — لاوامر التشغيل بالقروبات ⇐  ①\n\n — لاوامر التشغيل بالقناة  ⇐  ②""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                      InlineKeyboardButton(
                        "①", callback_data=f"tt"),
                    InlineKeyboardButton(
                        "②", callback_data=f"ddd"),
                    
                                                 ],
            ]

import asyncio
from pyrogram import Client, filters
from strings import get_command
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from YukkiMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


@app.on_message(
    command(["هادي"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/02ff5eed4dc2a34cbc1f7.jpg",
        caption=f"""- هادي مبرمج سورس ميوزك جاك .""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "هادي", url=f"https://t.me/jbbbbf"),
                ],[
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ʟᴜʀᴀ .", callback_data=f"fft"),
                ],
            ]
        ),
    )


@app.on_message(
    command(["انا مين"])
    & filters.group
    & ~filters.edited
)
async def khid(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/02ff5eed4dc2a34cbc1f7.jpg",
        caption=f"""انت يقلبي {message.from_user.mention()} 🙈🖤🥺""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "- sᴏᴜʀᴄᴇ ʟᴜʀᴀ .", url=f"https://t.me/jbbbbf"),
                ],
            ]
        ),
    )

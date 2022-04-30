@app.on_message(
    command(["مطور"])
    & filters.group
    & ~filters.edited
)
async def khalid(client: Client, message: Message):
    usr = await client.get_users(BOTID)
    name = usr.first_name
    async for photo in client.iter_profile_photos(BOTID, limit=1):
                    await message.reply_photo(photo.file_id,       caption=f"""[مطوري مشغول ياقلبي💞🥺](https://t.me/{OWNER})""", 
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        name, url=f"https://t.me/{OWNER}")
                ],[
                    InlineKeyboardButton(
                        "اضف البوت الي مجموعتك", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
                ],
            ]
        ),
    )

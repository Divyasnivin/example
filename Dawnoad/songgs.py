# Copyright (C) 2021 By Veez Music-Project

from __future__ import unicode_literals

import os

import requests
import wget
import yt_dlp
from driver.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL

from config import BOT_USERNAME as bn

ydl_opts = {
    "format": "best",
    "keepvideo": True,
    "prefer_ffmpeg": False,
    "geo_bypass": True,
    "outtmpl": "%(title)s.%(ext)s",
    "quite": True,
}

@Client.on_message(command(["song", f"song@Qznbot"]) & ~filters.edited)
def songg(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("** ابشر ثواني ويتحمل ..**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("** ما في اغنية بالعنوان ذا\n او تأكد من العنوان**")
        print(str(e))
        return
    m.edit("**تم لقيت لك **")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"****"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**ثواني وتنرسل الصوتية ..**")
        buttons = [[InlineKeyboardButton("JACK", url="t.me/kbbbd")]]
        reply_markup = InlineKeyboardMarkup(buttons)

        message.reply_audio(
            audio_file,
            caption=rep,
            reply_markup=reply_markup,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
            performer="Jack"
        )
        m.delete()
    except Exception as e:
        m.edit("خطأ")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

@Client.on_message(filters.command("صوت", [".", ""]) & ~filters.edited)
def song(_, message):
    query = " ".join(message.command[1:])
    m = message.reply("**ابشر ثواني وتنرسل**")
    ydl_ops = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        duration = results[0]["duration"]

    except Exception as e:
        m.edit("** ما في اغنية بالعنوان ذا\n او تأكد من العنوان**")
        print(str(e))
        return
    m.edit("**تم لقيت لك**")
    try:
        with yt_dlp.YoutubeDL(ydl_ops) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f"****"
        secmul, dur, dur_arr = 1, 0, duration.split(":")
        for i in range(len(dur_arr) - 1, -1, -1):
            dur += int(float(dur_arr[i])) * secmul
            secmul *= 60
        m.edit("**ثواني وتنرسل الصوتية**")
        buttons = [[InlineKeyboardButton("𝗌𝗈𝗎𝗋𝖼𝖾 𝗆𝗂𝗋𝖺", url="t.me/NvvvC")]]
        reply_markup = InlineKeyboardMarkup(buttons)

        message.reply_audio(
            audio_file,
            caption=rep,
            reply_markup=reply_markup,
            thumb=thumb_name,
            parse_mode="md",
            title=title,
            duration=dur,
            performer="Jack"
        )
        m.delete()
    except Exception as e:
        m.edit("خطأ")
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)


@Client.on_message(
    command(["vsong", f"vsong@Qznbot", "video", f"video@Qznbot"]) & ~filters.edited
)
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("**ثواني جالس يتحمل**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **حدث خطأ:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("**تاكيد التحميل ...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)


@Client.on_message(command(["lyric", f"lyric@{bn}"]))
async def lyrics(_, message):
    try:
        if len(message.command) < 2:
            await message.reply_text("» **give a lyric name too.**")
            return
        query = message.text.split(None, 1)[1]
        rep = await message.reply_text("**جاري البحث**..")
        resp = requests.get(
            f"https://api-tede.herokuapp.com/api/lirik?l={query}"
        ).json()
        result = f"{resp['data']}"
        await rep.edit(result)
    except Exception:
        await rep.edit(
            "❌ **results of lyric not found.**\n\n» **please give a valid song name.**"
        )

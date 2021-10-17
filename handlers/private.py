from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from config import BOT_USERNAME,CHANNEL_ID,GROUP_ID,  OWNER_ID
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/3f661bff9f20cb886d02c.jpg")
    await message.reply_text(
        f"""**Hey, I'm {bn}

I can play music in your group's voice call. Developed by [Hackelite](https://t.me/hackelite01).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "OWNER ", url="https://t.me/(OWNER_ID)")
                  ],[
                    InlineKeyboardButton(
                        "Group", url="https://t.me/(GROUP_ID)"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/(CHANNEL_ID)"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "Add To Your Group", url="https://t.me/(BOT_USERNAME)?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/(CHANNEL_ID)")
                ]
            ]
        )
   )



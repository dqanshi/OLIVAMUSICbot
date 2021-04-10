from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker("CAACAgQAAx0CTv65QgABBfJlYF6VCrGMm6OJ23AxHmD6qUSWESsAAhoQAAKm8XEeD5nrjz5IJFYeBA")
    await message.reply_text(
        f"""**Hey, I'm {bn} 馃幍

I can play music in your group's voice call. Developed by [Hackelite](https://t.me/hackelite01).

Add me to your group and play music freely!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "馃洜 Source Code 馃洜", url="https://t.me/mayank_ka_b_for_bot")
                  ],[
                    InlineKeyboardButton(
                        "馃挰 Group", url="https://t.me/hackelite02"
                    ),
                    InlineKeyboardButton(
                        "馃攰 Channel", url="https://t.me/hackelitebotlist"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "鉃� Add To Your Group 鉃�", url="https://t.me/TG_Group_Music_VC_V2_BOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Group Music Player Online 鉁�**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "馃攰 Channel", url="https://t.me/hackelitebotlist")
                ]
            ]
        )
   )



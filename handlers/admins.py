from asyncio.queues import QueueEmpty

from pyrogram import Client
from pyrogram.types import Message
from Oliva import Oliva

from config import BOT_NAME as BN
from helpers.filters import command, other_filters
from helpers.decorators import errors, authorized_users_only


@Client.on_message(command("pause") & other_filters)
@errors
@authorized_users_only
async def pause(_, message: Message):
    if (
            message.chat.id not in hackelite.pytgcalls.active_calls
    ) or (
            hackelite.pytgcalls.active_calls[message.chat.id] == 'paused'
    ):
        await message.reply_text("❗ Nothing is playing!")
    else:
        hackelite.pytgcalls.pause_stream(message.chat.id)
        await message.reply_text("▶️ Paused!")


@Client.on_message(command("resume") & other_filters)
@errors
@authorized_users_only
async def resume(_, message: Message):
    if (
            message.chat.id not in hackelite.pytgcalls.active_calls
    ) or (
            hackelite.pytgcalls.active_calls[message.chat.id] == 'playing'
    ):
        await message.reply_text("❗ Nothing is paused!")
    else:
        hackelite.pytgcalls.resume_stream(message.chat.id)
        await message.reply_text("⏸ Resumed!")


@Client.on_message(command("end") & other_filters)
@errors
@authorized_users_only
async def stop(_, message: Message):
    if message.chat.id not in hackelite.active_calls:
        await message.reply_text("❗ Nothing is streaming!")
    else:
        try:
            hackelite.queues.clear(message.chat.id)
        except QueueEmpty:
            pass

        hackelite.pytgcalls.leave_group_call(message.chat.id)
        await message.reply_text("❌ Stopped streaming!")


@Client.on_message(command("skip") & other_filters)
@errors
@authorized_users_only
async def skip(_, message: Message):
    if message.chat.id not in hackelite.pytgcalls.active_calls:
        await message.reply_text("❗ Nothing is playing to skip!")
    else:
        hackelite.queues.task_done(message.chat.id)

        if hackelite.queues.is_empty(message.chat.id):
            hackelite.pytgcalls.leave_group_call(message.chat.id)
        else:
            hackelite.pytgcalls.change_stream(
                message.chat.id,
                hackelite.queues.get(message.chat.id)["file"]
            )

        await message.reply_text("➡️ Skipped the current song!")

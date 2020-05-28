""".alive Plugin for @UniBorg"""
import asyncio
from telethon import events
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd


@borg.on(admin_cmd("alive"))
async def _(event):
    if event.fwd_from:
        return
    mentions = "**`𝔏𝔦𝔳𝔢 𝔞𝔰 𝔦𝔣 𝔶𝔬𝔲 𝔴𝔢𝔯𝔢 𝔱𝔬 𝔡𝔦𝔢 𝔱𝔬𝔪𝔬𝔯𝔯𝔬𝔴. 𝔏𝔢𝔞𝔯𝔫 𝔞𝔰 𝔦𝔣 𝔶𝔬𝔲 𝔴𝔢𝔯𝔢 𝔱𝔬 𝔩𝔦𝔳𝔢 𝔣𝔬𝔯𝔢𝔳𝔢𝔯.👍ɪ ᴀᴍ ᴀʟɪᴠᴇ ᴍʏ ᴍᴀꜱᴛᴇʀ🎈🎈`**\n\n**✅Telethon version:- 6.9.0**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**✅Python: 3.7.3**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**✅Bot Made By:- @itzSjDude\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n**✅Database Status:- Databases functioning normally!**\n◆ ▬▬▬▬▬▬ ❴✪❵ ▬▬▬▬▬▬ ◆\n💞Always with you, my peru master!\n"
    chat = await event.get_input_chat()
    async for x in borg.iter_participants(chat, filter=ChannelParticipantsAdmins):
        mentions += f""
    reply_message = None
    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        await reply_message.reply(mentions)
    else:
        await event.reply(mentions)
    await event.delete()

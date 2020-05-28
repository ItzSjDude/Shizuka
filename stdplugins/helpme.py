# For UniBorg
# Syntax .live
import sys
import os
import platform
import psutil
from telethon import events, functions, __version__
from uniborg.util import admin_cmd
from sql_helpers.global_variables_sql import SYNTAX, BUILD


@borg.on(admin_cmd(pattern="live ?(.*)", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    if Config.USER is not None:
        user = f"\n```User: {Config.USER}```"
    else:
        user = "ItzSjDude"
    uname = platform.uname()
    memory = psutil.virtual_memory()
    specs = f"```System: {uname.system}```\n```Release: {uname.release}```\n```Version: {uname.version}```\n```Processor: {uname.processor}```\n```Memory [RAM]: {get_size(memory.total)}```"
    help_string = f"`🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀\n`**General Account Analysis:**\n```🔧Build: {BUILD}```\nUser: {str(user)}\n```By: @R4v4n4```\n\n**⚙️System Specifications:**\n{specs}\n```🐍Python {sys.version}```\n```💾Telethon {__version__}```\n[🎀🎀🎀🎀🎀🎀🎀🎀🎀🎀](https://telegra.ph/file/b14a1e8b5698e0b3e933b.jpg)"    
    await event.reply(help_string + "\n\n")
    await event.delete()

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

SYNTAX.update({
    "help": "\
**Requested Module --> help**\
\n\n**Detailed usage of fuction(s):**\
\n\n```.help```\
\nUsage: Returns userbot's system stats, user's name (only if set).\
"
})
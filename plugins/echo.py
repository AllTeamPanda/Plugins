

from telethon.utils import get_display_name

from userbot._database.dB.echo_db import add_echo, check_echo, list_echo, rem_echo

from userbot._misc.managers import edit_delete, edit_or_reply
from userbot._misc.tools import inline_mention
from userbot import PandaBot
from userbot.modules.telethon import get_user_from_event

plugin_category = "modules"


@PandaBot.ilhammansiz_cmd(
    pattern="addecho$",
    command=("addecho", plugin_category),
    info={
        "header": "To repeat messages sent by the user.",
        "description": "Reply to user with this cmd so from then his every text and sticker messages will be repeated back to him.",
        "usage": "{tr}addecho <reply>",
    },
)
async def echo(e):
    r = await e.get_reply_message()
    if r:
        user = r.sender_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await edit_or_reply(e, "Reply To A user.")
    if check_echo(e.chat_id, user):
        return await edit_or_reply(e, "Echo already activated for this user.")
    add_echo(e.chat_id, user)
    ok = await e.client.get_entity(user)
    user = inline_mention(ok)
    await edit_or_reply(e, f"Activated Echo For {user}.")

    
    

@PandaBot.ilhammansiz_cmd(
    pattern="delecho$",
    command=("delecho", plugin_category),
    info={
        "header": "To stop repeating paticular user messages.",
        "description": "Reply to user with this cmd to stop repeating his messages back.",
        "usage": "{tr}delecho <reply>",
    },
)
async def rm(e):
    r = await e.get_reply_message()
    if r:
        user = r.sender_id
    else:
        try:
            user = e.text.split()[1]
            if user.startswith("@"):
                ok = await e.client.get_entity(user)
                user = ok.id
            else:
                user = int(user)
        except BaseException:
            return await edit_or_reply(e, "Reply To A User.")
    if check_echo(e.chat_id, user):
        rem_echo(e.chat_id, user)
        ok = await e.client.get_entity(user)
        user = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
        return await edit_or_reply(e, f"Deactivated Echo For {user}.")
    await edit_or_reply(e, "Echo not activated for this user")






@PandaBot.ilhammansiz_cmd(
    pattern="listecho( -a)?$",
    command=("listecho", plugin_category),
    info={
        "header": "shows the list of users for whom you enabled echo",
        "flags": {
            "a": "To list echoed users in all chats",
        },
        "usage": [
            "{tr}listecho",
            
        ],
    },
)
async def lstecho(e):
    if k := list_echo(e.chat_id):
        user = "**Activated Echo For Users:**\n\n"
        for x in k:
            ok = await e.client.get_entity(int(x))
            kk = f"[{get_display_name(ok)}](tg://user?id={ok.id})"
            user += f"•{kk}" + "\n"
        await edit_or_reply(e, user)
    else:
        await edit_or_reply(e, "`List is Empty, For echo`")
        

@PandaBot.ilhammansiz_cmd(incoming=True, edited=False)
async def samereply(event):
    if check_echo(event.chat_id, event.sender_id) and (
        event.message.text or event.message.sticker
    ):
        await event.reply(event.message)

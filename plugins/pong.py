import asyncio
from datetime import datetime

from ... import pandaub
from . import mention
from ..._misc.managers import edit_or_reply
from exportir import get_help



plugin_category = "plugins"


@pandaub.ilhammansiz_cmd(
    pattern="pong( -a|$)",
    command=("pong", plugin_category),
    info={
        "header": "Check How Long It Takes To Ping Your Userbot",
        "flags": {"-a": "average pong"},
        "usage": ["{tr}pong", "{tr}pong -a"],
    },
)
async def _(event):
    "To check ping"
    flag = event.pattern_match.group(1)
    start = datetime.now()
    if flag == " -a":
        pandaevent = await edit_or_reply(event, "`!....`")
        await asyncio.sleep(0.3)
        await pandaevent.edit("`🚶`")
        await asyncio.sleep(0.3)
        await pandaevent.edit("`🏃`")
        end = datetime.now()
        tms = (end - start).microseconds / 1000
        ms = round((tms - 0.6) / 3, 3)
        await pandaevent.edit(f"𝗣𝗶𝗻𝗴\n`{ms} ms`")
    else:
        pandaevent = await edit_or_reply(event, "🐼")
        await pandaevent.edit("⚡")
        await pandaevent.edit("👍")
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await pandaevent.edit(

            f"┣➠  __Pong:__ `{ms} ms`\n"
            f"┗➠ __Username:__ {mention} "
        )

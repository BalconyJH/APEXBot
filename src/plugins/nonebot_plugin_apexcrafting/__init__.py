from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, MessageEvent, MessageSegment
import time
import os
from .get_info import *
from .limit import *
from .html2pic import *

crafting = on_command("复制器", priority=12)
super_user = nonebot.get_driver().config.superusers



@crafting.handle()
async def _(bot: Bot, event: MessageEvent):
    userid = event.get_user_id()
    no_timeout, remain = check(event.get_user_id())
    if no_timeout or userid in super_user:
        data, condition = await get_data()
        html_text = await render(data)
        html_path = 'data/apex/crafting/'
        full_path = html_path + userid + '.html'
        file = open(full_path, 'w', encoding='utf-8')
        file.write(html_text)
        file.close()
        img = await htmltopic(full_path)
        await crafting.finish(MessageSegment.image(img), at_sender=True)

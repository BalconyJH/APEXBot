import time, random
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, MessageEvent, MessageSegment
import asyncio
from .get_info import *
from .limit import *
from .html2pic import *


predator = on_command('猎杀底分', aliases={'predator'}, priority=10)

super_user = nonebot.get_driver().config.superusers

@predator.handle()
async def _(bot: Bot, event: MessageEvent):
    userid = event.get_user_id()
    no_timeout, remain = check(userid)
    if no_timeout or userid in super_user:
        data, condition = await get_data()
        if condition == 200:
            html_text = await render(data)
            html_path = 'data/apex/Predator/'
            full_path = html_path + 'predator.html'
            file = open(full_path, 'w', encoding='utf-8')
            file.write(html_text)
            file.close()
            img = await htmltopic(full_path)
            await predator.finish(MessageSegment.image(img), at_sender=True)
            
        else:
            await predator.finish(message=f'错误码: {condition})')
    else:
        await predator.finish(message=f'还有{remain}秒可用')
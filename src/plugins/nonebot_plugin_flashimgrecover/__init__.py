#感谢Something For nothing（qq：3330883674）提供的部分源码
from nonebot import on_message
from nonebot.adapters.onebot.v11 import Bot, Event, MessageEvent
from nonebot.adapters.onebot.v11.message import Message
from nonebot.plugin import export
from nonebot.rule import Rule

export = export()
export.name = '防闪照小助手'
export.usage = '你发个闪照就知道了[]~(￣▽￣)~*'

async def _checker(bot: Bot, event: Event) -> bool:
    msg = str(event.get_message())
    return True if ('type=flash' in msg) and ('CQ:image' in msg) else False

flashimg = on_message(priority=50,rule=Rule(_checker))
@flashimg.handle()
async def flashimg_handle(bot: Bot, event: MessageEvent):
    if len(str(event.get_message())) < 100:
        msg = str(event.get_message()).replace(',type=flash', '').replace(',url=', '').replace('&#91;', '[').replace('&#93;', ']')
    else:
        msg = str(event.get_message()).replace(',type=flash', '').replace('&#91;', '[').replace('&#93;', ']')
    
    session_id = event.get_session_id()
    for superuser in bot.config.superusers:
        await bot.send_private_msg(user_id=superuser,message=f'来自{session_id}的闪照\n'+Message(msg))
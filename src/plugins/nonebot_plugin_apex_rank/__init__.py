from ..nonebot_plugin_apexlink.db import select
from .render import *

from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    Bot,
    Event,
    MessageEvent,
    MessageSegment,
    Message,
)
from nonebot.params import Arg, CommandArg, ArgPlainText

rank = on_command("段位", priority=90, block=False)


@rank.handle()
async def _(bot: Bot, event: Event, args: Message = CommandArg()):
    # 传入命令为空的话 cmds = "" , 不为空则为具体传入参数
    qq = event.get_user_id()
    # print("QQ:"+qq)
    username = args.extract_plain_text()
    # print("username"+username)
    if username == "":
        uid, platform = await select(int(qq))
        # print("UID:"+uid)
        if uid == None:
            await rank.finish(message="没绑定Origin ID你怎么查？", at_sender=True)
        else:
            data = await uid_data(uid, platform)
            html_text = await render(data)
            html_path = 'data/apex/htmls/'
            full_path = html_path + qq + '.html'
            file = open(full_path, 'w', encoding='utf-8')
            file.write(html_text)
            file.close()
            # print("fullpath:"+full_path)
            img = await htmltopic(full_path)
            await rank.finish(MessageSegment.image(img), at_sender=True)
    else:
        try:
            data = await get_data(username)
            html_text = await render(data)
            html_path = 'data/apex/htmls/'
            full_path = html_path + qq + '.html'
            file = open(full_path, 'w', encoding='utf-8')
            file.write(html_text)
            file.close()
            img = await htmltopic(full_path)
            # end=time.time()
            # print(end-st)
            await rank.finish(MessageSegment.image(img), at_sender=True)
        except KeyError:
            await rank.finish(message="没有找到该用户\n当前仅支持Origin ID查询", at_sender=True)

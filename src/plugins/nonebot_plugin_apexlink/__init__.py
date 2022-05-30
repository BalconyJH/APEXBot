from nonebot import on_command
from nonebot.adapters.onebot.v11 import (
    Bot,
    Event,
    MessageEvent,
    MessageSegment,
    Message,
)
from nonebot.params import Arg, CommandArg, ArgPlainText


from .db import *
from .get_info import *

link = on_command("绑定", aliases={"link"}, priority=100, block=False)


@link.handle()
async def _(bot: Bot, event: Event, args: Message = CommandArg()):
    # 通过用户发送消息获得 QQ 用户名 平台
    qq = event.get_user_id()
    commands = args.extract_plain_text()
    order = []
    order = commands.split(" ")
    username = order[0]
    # 将平台转换为大写
    platform = order[1].upper()
    # 得到用户名所对应的UID
    uid = await name_to_uid(username, platform)

    # await link.finish(message="{qq} {username} {platform}".format(qq=qq, username=username, platform=platform))

    """ 理想情况-能找到并获得uid  未实现用户名输入错误判断（已解决）"""

    # 保存用户信息至数据库
    if uid == "Error":
        await link.finish(
            message="绑定失败，" + username + " Not Found. 请确认Origin ID以及平台是否正确或者稍后重试", at_sender=True
        )
    else:
        await save_user_info(qq, uid, platform, username)

    # 查询数据库中是否已经绑定了origin_uid
    res, plat_form = await select(qq)
    """
    # print(res)
    # print(type(res))
    # print('==========================')
    # print(uid)
    # print(type(uid))
    """

    # 给用户输出返回 使用户知道自己是否成功绑定
    if res == uid:
        await link.finish(message="绑定成功", at_sender=True)
    else:
        await link.finish(message="绑定失败，请确认Origin ID以及平台是否正确或者稍后重试", at_sender=True)


"""
400	Try again in a few minutes.
403	Unauthorized / Unknown API key.
404	The player could not be found.
405	External API error.
410	Unknown platform provided.
429	Rate limit reached.
500	Internal error.
"""

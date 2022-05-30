import time
import nonebot
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, MessageEvent, MessageSegment, Message
from nonebot.params import Arg, CommandArg, ArgPlainText

help = on_command('help', aliases={'菜单', '?'}, block=False, priority=10)

@help.handle()
async def _(event: Event, args: Message = CommandArg()):
    command_name = args.extract_plain_text()
    if command_name == "":
        msg = {"欢迎使用ApexBot\n"
                "支持使用的前缀：/\n"
                "/help  # 获取本插件帮助\n"
                "/help list  # 展示已加载插件列表\n"
                "/help <Command>  # 调取目标插件帮助信息"}
        await help.finish(msg)
    elif command_name == "list":
        msg = {"已加载插件列表：\n"
                "/段位\n"
                "/地图\n"
                "/绑定\n"
                "/复制器\n"
                "/猎杀底分\n"
                "/赞助\n"
                "bilibili直播及动态推送"}
        await help.finish(msg)
    elif command_name == "段位":
        msg = { "命令名：段位\n"
                "功能：查询您的段位及基础信息\n"
                "使用方法：/段位 Origin_ID\n"
                "示例：/段位 flymao2\n"
                "Tips：Origin_ID不区分大小写"}
        await help.finish(msg)
    elif command_name == "地图":
        msg = { "命令名：地图\n"
                "功能：查询实时地图信息\n"
                "使用方法：/地图\n"
                "示例：/地图"}
        await help.finish(msg)
    elif command_name == "绑定":
        msg = { "命令名：绑定\n"
                "功能：将您的QQ绑定到指定Origin账户，方便自身查询\n"
                "使用方法：/绑定 Origin_ID [PC/PS4/X1]\n"
                "示例：/绑定 flymao2 PC\n"
                "Tips：暂时无法解绑，但是可以覆盖绑定账户"}
        await help.finish(msg)
    elif command_name == "复制器":
        msg = { "命令名：复制器\n"
                "功能：查询当前复制器信息\n"
                "使用方法：/复制器\n"
                "示例：/复制器"}
        await help.finish(msg)
    elif command_name == "猎杀底分":
        msg = { "命令名：猎杀底分\n"
                "功能：查询当前猎杀底分\n"
                "使用方法：/猎杀底分\n"
                "示例：/猎杀底分\n"
                "Tips：分数数据每小时更新一次"}
        await help.finish(msg)
    elif command_name == "赞助":
        msg = { "命令名：赞助\n"
                "功能：为作者发电，以便更好的创作及服务\n"
                "使用方法：/赞助\n"
                "示例：/赞助"}
        await help.finish(msg)

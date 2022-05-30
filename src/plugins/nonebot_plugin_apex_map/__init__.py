import time
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, MessageEvent, MessageSegment, Message
from nonebot.params import Arg, CommandArg, ArgPlainText
from .get_info import get_map, current_Map, remaining_Timer, next_Map


# 地图轮换
mapQuery = on_command('地图', aliases={'map'}, priority=95, block=False)

@mapQuery.handle()
async def queryMaps(bot: Bot):
    map_data = await get_map()
    currentMap = await current_Map(map_data)
    remainingTimer = await remaining_Timer(map_data)
    nextMap = await next_Map(map_data)

    if currentMap == 'Olympus':
        currentMap = '奥林匹斯'
    elif currentMap == 'Kings Canyon':
        currentMap = '诸王峡谷'
    elif currentMap == "World's Edge":
        currentMap = '世界尽头'
    elif currentMap == 'Storm Point':
        currentMap = '风暴点'

    if nextMap == 'Olympus':
        nextMap = '奥林匹斯'
    elif nextMap == 'Kings Canyon':
        nextMap = '诸王峡谷'
    elif nextMap == "World's Edge":
        nextMap = '世界尽头'
    elif nextMap == 'Storm Point':
        nextMap = '风暴点'

    await mapQuery.finish(message=f'当前的匹配地图为: {currentMap}\n当前地图剩余时间: {remainingTimer}\n下一张匹配地图为: {nextMap}')

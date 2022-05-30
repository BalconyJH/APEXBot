'''
 # @Author      : Kiss-your
 # @Date        : 2022-05-22 20:41:34
 # @LastEditTime: 2022-05-30 14:38:32
 # @LastEditors : Kiss-your
 # @Description : 
 # @GitHub      : https://github.com/Kiss-your
'''
import json
import requests


apikey = nonebot.get_driver().config.apex_key
async def get_map():
    # apikey = nonebot.get_driver().config.apex_key
    url = f'https://api.mozambiquehe.re/maprotation?version=5&auth={apikey}'
    map_data = requests.get(url)
    return map_data.text
# 获取当前地图
async def current_Map(map):
    map_data = json.loads(map)
    currentMap = map_data['battle_royale']['current']['map']
    return currentMap
# 获取剩余时间
async def remaining_Timer(map):
    map_data = json.loads(map)
    remainingTimer = map_data['battle_royale']['current']['remainingTimer']
    return remainingTimer
# 获取下一张地图
async def next_Map(map):
    map_data = json.loads(map)
    nextMap = map_data['battle_royale']['next']['map']
    return nextMap

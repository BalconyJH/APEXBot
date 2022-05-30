import os.path
import webbrowser

import jinja2
from pathlib import Path
import random
from playwright.async_api import Page, Browser, async_playwright, Error
import asyncio

from .get_info import *

'''
template_to_html = require("nonebot_plugin_htmlrender").template_to_html
html_to_pic = require("nonebot_plugin_htmlrender").html_to_pic


def renderhtml(status, user_name, user_level, toNextLevelPercent, rank_Img, rank_Name, rank_Score, ladder,
               arenarank_Img, arenarank_Name, arenarank_Score, arenaladder, selected_Legend, lobby_State, is_Online,
               is_InGame, can_Join, party_Full,
               currentState_AsText, ):
    TEMPLATES_PATH = str(Path(__file__).parent / "templates")
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
        enable_async=False,
    )

    template = env.get_template('crafting.html')  # 获取一个模板文件

    element = {
        'status': status,
        'name': user_name,
        'level': user_level,
        'toNextLevelPercent': toNextLevelPercent,
        'rankImg': rank_Img,
        'rankName': rank_Name,
        'rankScore': rank_Score,
        'ladderPosPlatform': ladder,
        'arenarankImg': arenarank_Img,
        'arenarankName': arenarank_Name,
        'arenarankScore': arenarank_Score,
        'ladderPlatform': arenaladder,
        'selectedLegend': selected_Legend,
        'lobbyState': lobby_State,
        'isOnline': is_Online,
        'isInGame': is_InGame,
        'canJoin': can_Join,
        'partyFull': party_Full,
        'currentStateAsText': currentState_AsText,
    }
    test = template.render(element)
    return test

'''
'''
userhtml = renderhtml(status='status_offline', user_name='flymao2', user_level=123, toNextLevelPercent='34', rank_Name='铂金',
                      rank_Score='55555',
                      ladder=34,
                      arenarank_Name='钻石', arenarank_Score='66666', arenaladder='1', lobby_State='是', is_Online='是',
                      is_InGame='否',
                      can_Join='否', party_Full='是', currentState_AsText='in match(3:22)',
                      rank_Img="https:\/\/api.mozambiquehe.re\/assets\/ranks\/bronze2.png",
                      arenarank_Img='https:\/\/api.mozambiquehe.re\/assets\/ranks\/unranked4.png',
                      selected_Legend='https:\/\/api.mozambiquehe.re\/assets\/icons\/bloodhound.png')
print(userhtml)
'''


async def render(data):
    data = data

    # 数据处理与获取
    status = 'status_online'
    user_status = await userstatus(data)
    user_name = await username(data)
    user_level = await userlevel(data)
    toNextLevelPercent = await toNextLevel(data)
    rank_Img = await rankImg(data)
    rank_Name = await rankName(data)
    rank_Score = await rankScore(data)
    ladder = await ladderPosPlatform(data)
    arenarank_Img = await arenarankImg(data)
    arenarank_Name = await arenarankName(data)
    arenarank_Score = await arenarankScore(data)
    arenaladder = await arenaladderPosPlatform(data)
    selected_Legend = await selectedLegend(data)
    lobby_State = await lobbyState(data)
    is_Online = await isOnline(data)
    is_InGame = await isInGame(data)
    can_Join = await  canJoin(data)
    party_Full = await partyFull(data)
    currentState_AsText = await currentStateAsText(data)

    # 数据格式化

    # 用户状态
    if user_status == 'offline':
        status = 'status_offline'
    elif user_status == 'inLobby':
        status = 'status_online'
    else:
        status = 'status_ingame'

    # 段位名字
    if rank_Name == 'Apex Predator':
        rank_Name = 'APEX猎杀者'
    elif rank_Name == 'Master':
        rank_Name = '大师'
    elif rank_Name == 'Diamond':
        rank_Name = '钻石'
    elif rank_Name == 'Platinum':
        rank_Name = '铂金'
    elif rank_Name == 'Gold':
        rank_Name = '黄金'
    elif rank_Name == 'Silver':
        rank_Name = '白银'
    elif rank_Name == 'Bronze':
        rank_Name = '青铜'

    # 竞技场段位名字
    if arenarank_Name == 'Apex Predator':
        arenarank_Name = 'APEX猎杀者'
    elif arenarank_Name == 'Master':
        arenarank_Name = '大师'
    elif arenarank_Name == 'Diamond':
        arenarank_Name = '钻石'
    elif arenarank_Name == 'Platinum':
        arenarank_Name = '铂金'
    elif arenarank_Name == 'Gold':
        arenarank_Name = '黄金'
    elif arenarank_Name == 'Silver':
        arenarank_Name = '白银'
    elif arenarank_Name == 'Bronze':
        arenarank_Name = '青铜'

    # 猎杀排名
    if ladder == -1:
        ladder = '未排名'

    # 猎杀排名
    if arenaladder == -1:
        arenaladder = '未排名'

    # 大厅状态
    if lobby_State == 'open':
        lobby_State = '打开'
    else:
        lobby_State = '邀请'

    # 在线状态
    if is_Online == '1':
        is_Online = '在线'
    else:
        is_Online = '离线'

    # 游戏状态
    if is_InGame == '1':
        is_InGame = '正在游戏'
    else:
        is_InGame = '未在游戏'

    # 游戏状态
    if can_Join == '1':
        can_Join = '是'
    else:
        can_Join = '否'

    # 游戏状态
    if party_Full == '1':
        party_Full = '是'
    else:
        party_Full = '否'

    TEMPLATES_PATH = str(Path(__file__).parent / "templates")
    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(TEMPLATES_PATH),
        enable_async=True,
    )

    template = env.get_template('demo.html')  # 获取一个模板文件
    element = {
        'status': status,
        'name': user_name,
        'level': user_level,
        'toNextLevelPercent': toNextLevelPercent,
        'rankImg': rank_Img,
        'rankName': rank_Name,
        'rankScore': rank_Score,
        'ladderPosPlatform': ladder,
        'arenarankImg': arenarank_Img,
        'arenarankName': arenarank_Name,
        'arenarankScore': arenarank_Score,
        'ladderPlatform': arenaladder,
        'selectedLegend': selected_Legend,
        'lobbyState': lobby_State,
        'isOnline': is_Online,
        'isInGame': is_InGame,
        'canJoin': can_Join,
        'partyFull': party_Full,
        'currentStateAsText': currentState_AsText,
    }
    test = await template.render_async(element)
    # print(test)
    return test


async def htmltopic(path):
    fullpath = path
    async with async_playwright() as p:
        browser_type = p.chromium
        browser = await browser_type.launch()
        page = await browser.new_page(viewport={"width": 900, "height": 700})
        await page.goto('file:///' + os.path.abspath(fullpath))
        img = await page.screenshot(full_page=True)
        await page.close()

    return img

import requests
import json
import nonebot


apikey = nonebot.get_driver().config.apex_key
#UID查询
async def uid_data(uid, platform):
    url = f"https://api.mozambiquehe.re/bridge?platform={platform}&uid={uid}&auth={apikey}"

    data = requests.get(url)
    condition = data.status_code
    return data.text



#   获取网页代码并保存
async def get_data(playername):
    url = f"https://api.mozambiquehe.re/bridge?version=5&platform=PC&player={playername}&auth={apikey}"

    data = requests.get(url)
    state = data.status_code
    return data.text

async def userstatus(data):
    user_data = json.loads(data)
    user_status = user_data['realtime']['currentState']
    return user_status


async def username(data):
    user_data = json.loads(data)
    user_name = user_data['global']['name']
    return user_name


async def userlevel(data):
    user_data = json.loads(data)
    user_level = user_data['global']['level']
    return user_level


async def toNextLevel(data):
    user_data = json.loads(data)
    toNextLevelPercent = user_data['global']['toNextLevelPercent']
    return toNextLevelPercent


async def rankImg(data):
    user_data = json.loads(data)
    rank_Img = user_data['global']['rank']['rankImg']
    return rank_Img


async def rankName(data):
    user_data = json.loads(data)
    rank_Name = user_data['global']['rank']['rankName']
    return rank_Name


async def rankScore(data):
    user_data = json.loads(data)
    rank_Score = user_data['global']['rank']['rankScore']
    return rank_Score


async def ladderPosPlatform(data):
    user_data = json.loads(data)
    ladder = user_data['global']['rank']['ladderPosPlatform']
    return ladder


async def arenarankImg(data):
    user_data = json.loads(data)
    arenarank_Img = user_data['global']['arena']['rankImg']
    return arenarank_Img


async def arenarankName(data):
    user_data = json.loads(data)
    arenarank_Name = user_data['global']['arena']['rankName']
    return arenarank_Name


async def arenarankScore(data):
    user_data = json.loads(data)
    arenarank_Score = user_data['global']['arena']['rankScore']
    return arenarank_Score


async def arenaladderPosPlatform(data):
    user_data = json.loads(data)
    arenaladder = user_data['global']['arena']['ladderPosPlatform']
    return arenaladder


async def selectedLegend(data):
    user_data = json.loads(data)
    selected_Legend = user_data['legends']['selected']['ImgAssets']['icon']
    return selected_Legend


async def lobbyState(data):
    user_data = json.loads(data)
    lobby_State = user_data['realtime']['lobbyState']
    return lobby_State


async def isOnline(data):
    user_data = json.loads(data)
    is_Online = user_data['realtime']['isOnline']
    return is_Online


async def isInGame(data):
    user_data = json.loads(data)
    is_InGame = user_data['realtime']['isInGame']
    return is_InGame


async def canJoin(data):
    user_data = json.loads(data)
    can_Join = user_data['realtime']['canJoin']
    return can_Join


async def partyFull(data):
    user_data = json.loads(data)
    party_Full = user_data['realtime']['partyFull']
    return party_Full


async def currentStateAsText(data):
    user_data = json.loads(data)
    currentState_AsText = user_data['realtime']['currentStateAsText']
    return currentState_AsText


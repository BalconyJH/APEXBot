'''
 # @Author      : Kiss-your
 # @Date        : 2022-05-22 20:41:41
 # @LastEditTime: 2022-05-30 14:38:52
 # @LastEditors : Kiss-your
 # @Description : 
 # @GitHub      : https://github.com/Kiss-your
'''
import requests
import nonebot
import json


async def get_data():
    apikey = nonebot.get_driver().config.apex_key
    url = f'https://api.mozambiquehe.re/crafting?&auth={apikey}'
    data = requests.get(url)
    condition = data.status_code
    return data.text,condition

async def dailycrafting1_img(data):
    craftingdata = json.loads(data)
    dailycrafting1img = craftingdata[0]['bundleContent'][0]['itemType']['asset']
    return dailycrafting1img

async def dailycrafting2_img(data):
    craftingdata = json.loads(data)
    dailycrafting2img = craftingdata[0]['bundleContent'][1]['itemType']['asset']
    return dailycrafting2img

async def dailycrafting1_name(data):
    craftingdata = json.loads(data)
    dailycrafting1name = craftingdata[0]['bundleContent'][0]['itemType']['name']
    return dailycrafting1name

async def dailycrafting2_name(data):
    craftingdata = json.loads(data)
    dailycrafting2name = craftingdata[0]['bundleContent'][1]['itemType']['name']
    return dailycrafting2name

async def dailycrafting1_cost(data):
    craftingdata = json.loads(data)
    dailycrafting1cost = craftingdata[0]['bundleContent'][0]['cost']
    return dailycrafting1cost

async def dailycrafting2_cost(data):
    craftingdata = json.loads(data)
    dailycrafting2cost = craftingdata[0]['bundleContent'][1]['cost']
    return dailycrafting2cost


async def weeklycrafting1_img(data):
    craftingdata = json.loads(data)
    weeklycrafting1img = craftingdata[1]['bundleContent'][0]['itemType']['asset']
    return weeklycrafting1img

async def weeklycrafting2_img(data):
    craftingdata = json.loads(data)
    weeklycrafting2img = craftingdata[1]['bundleContent'][1]['itemType']['asset']
    return weeklycrafting2img

async def weeklycrafting1_name(data):
    craftingdata = json.loads(data)
    weeklycrafting1name = craftingdata[1]['bundleContent'][0]['itemType']['name']
    return weeklycrafting1name

async def weeklycrafting2_name(data):
    craftingdata = json.loads(data)
    weeklycrafting2name = craftingdata[1]['bundleContent'][1]['itemType']['name']
    return weeklycrafting2name

async def weeklycrafting1_cost(data):
    craftingdata = json.loads(data)
    weeklycrafting1cost = craftingdata[1]['bundleContent'][0]['cost']
    return weeklycrafting1cost

async def weeklycrafting2_cost(data):
    craftingdata = json.loads(data)
    weeklycrafting2cost = craftingdata[1]['bundleContent'][1]['cost']
    return weeklycrafting2cost

async def time_Remain1(data):
    craftingdata = json.loads(data)
    timeRemain1 = craftingdata[0]['end']
    return timeRemain1

async def time_Remain2(data):
    craftingdata = json.loads(data)
    timeRemain2 = craftingdata[1]['end']
    return timeRemain2
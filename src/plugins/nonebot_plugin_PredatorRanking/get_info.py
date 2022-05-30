import json
import requests
import asyncio
import nonebot


#  猎杀底分查询
async def get_data():
    apikey = nonebot.get_driver().config.apex_key
    url = "https://api.mozambiquehe.re/predator?auth=" + apikey
    data = requests.get(url)
    state = data.status_code
    return data.text, state

async def rp_data(data):
    predator_data = json.loads(data)

    pc_foundrank_rp = predator_data['RP']['PC']['foundRank']
    pc_val_rp = predator_data['RP']['PC']['val']
    pc_totalMastersAndPreds_rp = predator_data['RP']['PC']['totalMastersAndPreds']
    ps4_foundrank_rp = predator_data['RP']['PS4']['foundRank']
    ps4_val_rp = predator_data['RP']['PS4']['val']
    ps4_totalMastersAndPreds_rp = predator_data['RP']['PS4']['totalMastersAndPreds']
    x1_foundrank_rp = predator_data['RP']['X1']['foundRank']
    x1_val_rp = predator_data['RP']['X1']['val']
    x1_totalMastersAndPreds_rp = predator_data['RP']['X1']['totalMastersAndPreds']
    switch_foundrank_rp = predator_data['RP']['SWITCH']['foundRank']
    switch_val_rp = predator_data['RP']['SWITCH']['val']
    switch_totalMastersAndPreds_rp = predator_data['RP']['SWITCH']['totalMastersAndPreds']
    return pc_foundrank_rp, pc_val_rp, ps4_foundrank_rp, ps4_val_rp, x1_foundrank_rp, x1_val_rp, switch_foundrank_rp, switch_val_rp, pc_totalMastersAndPreds_rp, ps4_totalMastersAndPreds_rp, x1_totalMastersAndPreds_rp, switch_totalMastersAndPreds_rp

async def ap_data(data):
    predator_data = json.loads(data)

    pc_foundrank_ap = predator_data['AP']['PC']['foundRank']
    pc_val_ap = predator_data['AP']['PC']['val']
    pc_totalMastersAndPreds_ap = predator_data['AP']['PC']['totalMastersAndPreds']
    ps4_foundrank_ap = predator_data['AP']['PS4']['foundRank']
    ps4_val_ap = predator_data['AP']['PS4']['val']
    ps4_totalMastersAndPreds_ap = predator_data['AP']['PS4']['totalMastersAndPreds']
    x1_foundrank_ap = predator_data['AP']['X1']['foundRank']
    x1_val_ap = predator_data['AP']['X1']['val']
    x1_totalMastersAndPreds_ap = predator_data['AP']['X1']['totalMastersAndPreds']
    switch_foundrank_ap = predator_data['AP']['SWITCH']['foundRank']
    switch_val_ap = predator_data['AP']['SWITCH']['val']
    switch_totalMastersAndPreds_ap = predator_data['AP']['SWITCH']['totalMastersAndPreds']
    return pc_foundrank_ap, pc_val_ap, ps4_foundrank_ap, ps4_val_ap, x1_foundrank_ap, x1_val_ap, switch_foundrank_ap, switch_val_ap, pc_totalMastersAndPreds_ap, ps4_totalMastersAndPreds_ap, x1_totalMastersAndPreds_ap, switch_totalMastersAndPreds_ap
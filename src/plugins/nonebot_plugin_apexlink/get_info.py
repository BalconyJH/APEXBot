'''
 # @Author      : Kiss-your
 # @Date        : 2022-05-22 20:41:36
 # @LastEditTime: 2022-05-30 14:39:27
 # @LastEditors : Kiss-your
 # @Description : 
 # @GitHub      : https://github.com/Kiss-your
'''
import json
import nonebot
import requests

# https://api.mozambiquehe.re/bridge?auth=nDnEVcxUzoanUYmLFzTc&uid=2535462396366855&platform=X1&enableClubsBeta=true

apikey = nonebot.get_driver().config.apex_key
# 名字转换为UID
async def name_to_uid(playername, platform):
    playername = playername
    plat_form = platform
    url = (
        f"https://api.mozambiquehe.re/nametouid?auth={apikey}&player="
        + playername
        + "&platform="
        + plat_form
    )
    data = requests.get(url)
    data = json.loads(data.text)
    if plat_form == "PC":
        try:
            uid = data["uid"]
        except:
            uid = "Error"
    else:
        try:
            uid = data["result"]
        except:
            uid = "Error"
    return str(uid)


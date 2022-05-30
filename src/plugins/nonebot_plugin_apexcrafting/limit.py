from datetime import datetime
import json
import nonebot

query_cd = nonebot.get_driver().config.query_cd


# 读
def readjson():
    with open(r'data/json/timeControl.json', 'r') as f_in:
        data = json.load(f_in)
        f_in.close()
        return data


# 写
def writejson(qid: str, time: int, data: dict):
    data[qid] = time
    with open(r'data/json/timeControl.json', 'w') as f_out:
        json.dump(data, f_out)
        f_out.close()


# 删
def deletejson(qid: str, data: dict):
    del data[qid]
    with open(r'data/json/timeControl.json', 'w') as f_out:
        json.dump(data, f_out)
        f_out.close()


# 查
def check(user_id) -> 'bool,int':
    data = readjson()
    if user_id in data:
        last_time = datetime.strptime(data[user_id], "%Y-%m-%d %H:%M:%S")
        this_time = datetime.now()
        timespan = (this_time - last_time).total_seconds()
        if timespan > query_cd:
            writejson(user_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data)
            return True, 0
        else:
            return False, query_cd - timespan
    else:
        writejson(user_id, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), data)
        return True, 0

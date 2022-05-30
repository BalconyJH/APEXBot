from typing import Optional
from nonebot.adapters.onebot.v11.message import MessageSegment, Message
from pydantic import BaseModel, root_validator
# from pydantic import Json

from .desc import Desc
# from .card import Card
# from .display import Display


class Dynamic(BaseModel):
    desc: Desc
    # card: Json[Card]  # type: ignore
    # extend_json: Json[Dict] # 不知道干什么的
    # display: Display

    type: int = 0
    id: int = 0
    url: str = ""
    time: int = 0
    uid: int = 0
    name: str = ""
    message: Optional[Message]

    @root_validator()
    def set_args(cls, values):
        values["type"] = values["desc"].type
        values["id"] = values["desc"].dynamic_id
        values["url"] = f"https://t.bilibili.com/{values['id']}"
        values["time"] = values["desc"].timestamp
        values["uid"] = values["desc"].user_profile.info.uid
        values["name"] = values["desc"].user_profile.info.uname
        return values

    async def format(self, img):
        type_msg = {
            0: "发布了新动态",
            1: "转发了一条动态",
            8: "发布了新投稿",
            16: "发布了短视频",
            64: "发布了新专栏",
            256: "发布了新音频",
        }
        if self.uid == 30790219:
            self.message = (
                    f"{self.name} "
                    + f"{type_msg.get(self.type, type_msg[0])}：\n"
                    + MessageSegment.image(f"base64://{img}")
                    + MessageSegment.text("视频链接：\n")
                    + f"{self.url}\n"
                    + "更多APEX知识/技巧/教学： https://afdian.net/@SvenAPEX"
            )
        elif self.uid == 59477825:
            self.message = (
                    f"{self.name} "
                    + f"{type_msg.get(self.type, type_msg[0])}：\n"
                    + MessageSegment.image(f"base64://{img}")
                    + MessageSegment.text("视频链接：\n")
                    + f"{self.url}\n"
                    + "个人主页： https://space.bilibili.com/59477825"
            )
        else:
            self.message = (
                f"{self.name} "
                + f"{type_msg.get(self.type, type_msg[0])}：\n"
                + f"{self.url}\n"
                + MessageSegment.image(f"base64://{img}")
            )

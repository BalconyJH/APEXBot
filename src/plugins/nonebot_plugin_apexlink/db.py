from platform import platform
from pymysql import IntegrityError
from sqlalchemy import BIGINT, Column, String, create_engine, true
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# 创建对象的基类:
Base = declarative_base()


class qq2origin(Base):
    __tablename__ = "qq2origin_id"
    qq_account = Column(String(20), primary_key=True)
    origin_uid = Column(String(30))
    platform = Column(String(255))
    username = Column(String(30))


# 创建引擎,初始化数据库连接:
engine = create_engine(
    "mysql+pymysql://leon:leon0511@10.0.16.3:3306/apexbot"
)

DBSession = sessionmaker(bind=engine)

# 查
async def select(qq: int):
    """通过 QQ 获得数据库中是否绑定了 origin_uid"""
    session = DBSession()
    res = session.query(qq2origin).filter(qq2origin.qq_account == qq).first()
    session.close()
    try:
        return res.origin_uid, res.platform
    except AttributeError:
        return None, None


# 增/改
async def save_user_info(
    qq: int, origin_uid: int, platform: str = "", username: str = ""
):
    """保存用户信息"""
    session = DBSession()
    res = session.query(qq2origin).filter(qq2origin.qq_account == qq).first()
    if res != None:
        res = session.merge(
            qq2origin(
                qq_account=qq,
                origin_uid=origin_uid,
                platform=platform,
                username=username,
            )
        )
    else:
        res = session.add(
            qq2origin(
                qq_account=qq,
                origin_uid=origin_uid,
                platform=platform,
                username=username,
            )
        )
    session.commit()
    session.close()
    return res

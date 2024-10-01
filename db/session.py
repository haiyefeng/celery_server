from urllib.parse import unquote
from functools import wraps

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

MYSQL_DSN = settings.mysql_dsn
SQLALCHEMY_MYSQL_DSN = (
    f"mysql+pymysql://{MYSQL_DSN.username}:{unquote(MYSQL_DSN.password)}@"
    f"{MYSQL_DSN.host}:{MYSQL_DSN.port}{MYSQL_DSN.path}"
)

engine = create_engine(
    SQLALCHEMY_MYSQL_DSN,
    pool_size=10,
    max_overflow=20,
    pool_timeout=30,
    pool_recycle=3600,
)
Session = sessionmaker(
    engine, autoflush=False, expire_on_commit=False
)  # 设置不自动flush和提交后过期数据


def provide_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 如果 kwargs 中没有 session，则创建一个新的
        if "session" not in kwargs:
            with Session.begin() as session:  # 自动开始和提交事务
                kwargs["session"] = session
                return func(*args, **kwargs)  # 调用原始函数
        else:
            # 已有session，直接传递给原始函数
            return func(*args, **kwargs)

    return wrapper

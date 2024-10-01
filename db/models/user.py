from sqlalchemy import (
    Integer,
    String,
    Boolean,
)
from sqlalchemy.orm import mapped_column, validates
from db.models import Model


class User(Model):
    """用户"""

    __tablename__ = "user"
    id = mapped_column(Integer, primary_key=True, autoincrement=True)  # 自增主键
    username = mapped_column(
        String(32), doc="用户名"
    )  # 该注释仅用于python侧使用，如类的__doc__
    email = mapped_column(String(32), comment="邮箱")  # 该注释会写入数据库
    phone = mapped_column(String(16), doc="手机号")
    is_superuser = mapped_column(Boolean, default=False, doc="是否为超级用户")
    is_enabled = mapped_column(Boolean, default=True, doc="是否有效")

    @validates("email")
    def validate_email(self, key, address):
        assert "@" in address
        return address

    @validates("phone")
    def validate_phone(self, key, phone_number):
        pattern = re.compile(r"1[356789]\d{9}")
        ret = pattern.match(phone_number)
        assert ret, "手机号不符合格式要求，请输入合法的手机号后再次提交！"
        return phone_number

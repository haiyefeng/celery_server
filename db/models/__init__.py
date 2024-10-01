from datetime import datetime

from sqlalchemy import (
    String,
    Boolean,
    DateTime,
)
from sqlalchemy.orm import DeclarativeBase, mapped_column


class Base(DeclarativeBase):
    pass


class Model(Base):
    __abstract__ = True
    create_at = mapped_column(DateTime, default=datetime.now)
    creator = mapped_column(String(30))
    updated_at = mapped_column(DateTime, onupdate=datetime.now)
    updated_by = mapped_column(String(30))
    is_deleted = mapped_column(Boolean, default=False)

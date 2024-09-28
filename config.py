from typing import Any, Callable, Set

from pydantic import (
    AliasChoices,
    AmqpDsn,
    BaseModel,
    Field,
    ImportString,
    MySQLDsn,
    RedisDsn,
)

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mysql_dsn: MySQLDsn = None
    amqp_dsn: int = None
    redis_dsn: RedisDsn = None

    model_config = SettingsConfigDict(env_prefix="fund_sync", env_file=".env")


settings = Settings()

from pydantic import PostgresDsn, field_validator
from pydantic_settings import BaseSettings


class AppSettings(BaseSettings):
    database_url: PostgresDsn
    uvicorn_reload: int = 0
    uvicorn_workers: int = 4

    @field_validator('database_url')
    def database_url_driver_is_asyncpg(cls, v: PostgresDsn):
        assert v and v.unicode_string().startswith("postgresql+asyncpg"), "`database_url` must use the asyncpg driver"
        return v

settings = AppSettings() # type: ignore

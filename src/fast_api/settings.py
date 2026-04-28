from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_confi = SettingsConfigDict(
        env_file='.env', env_file_encoding='utf-8'
    )
    DATABASE_URL: str

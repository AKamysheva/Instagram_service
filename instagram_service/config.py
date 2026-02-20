from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    SECRET_KEY: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    DEBUG: bool
    INSTAGRAM_USER_ACCESS_TOKEN: str
    INSTAGRAM_USER_ID: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()

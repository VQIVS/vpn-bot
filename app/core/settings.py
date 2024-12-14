from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings


class DBSettings(BaseModel):
    host: str | None = "localhost"
    port: int | None = 5432
    user: str | None = "postgres"
    password: str | None = "postgres"
    database: str | None = "postgres"


class BotSettings(BaseModel):
    token: str | None = None


class Settings(BaseSettings):
    db: DBSettings = Field(default_factory=DBSettings)
    bot: BotSettings = Field(default_factory=BotSettings)

    class Config:
        env_file = ".env"


settings = Settings()

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URL: str = "sqlite:///./authon_stock.db"

    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Stock Automation API"
    model_config = SettingsConfigDict(
        env_file=".env", case_sensitive=True, extra="ignore"
    )

    SMTP_HOST: str | None = None
    SMTP_PORT: int | None = None
    SMTP_USER: str | None = None
    SMTP_PASSWORD: str | None = None
    EMAIL_FROM: str | None = None

    ALERT_EMAILS: str | None = None
    ALERT_PHONE: str | None = None

    N8N_WEBHOOK_URL: str | None = None


settings = Settings()

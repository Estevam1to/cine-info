from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings managed by Pydantic.
    Values are loaded from environment variables.
    """

    GOOGLE_API_KEY: str
    GOOGLE_API_MODEL: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False


settings = Settings()

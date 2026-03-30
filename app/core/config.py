from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "MyProject"
    database_url: str = "postgresql+psycopg://postgres:postgres@localhost:5432/myproject"
    elasticsearch_url: str = "http://localhost:9200"
    elasticsearch_index: str = "articles"
    openai_api_key: str = ""
    openai_base_url: str = "https://api.openai.com/v1"
    openai_model: str = "gpt-4o-mini"
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

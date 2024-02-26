from typing import Any
from enum import Enum
from pydantic import PostgresDsn, RedisDsn, root_validator
from pydantic_settings import BaseSettings

class Environment(str, Enum):
    DEV = "DEV"
    TESTING = "TESTING"
    PRODUCTION = "PRODUCTION"

    @property
    def is_debug(self):
        return self in (self.DEV, self.TESTING)

    @property
    def is_testing(self):
        return self == self.TESTING
    
    @property
    def is_prod(self):
        return self == self.PRODUCTION

class Config(BaseSettings):
    ENVIRONMENT: Environment = Environment.DEV

    APP_NAME: str = "app"

    OPENSEARCH_HOST: str = "localhost"
    OPENSEARCH_PORT: int = 9200
    OPENSEARCH_USERNAME: str = "admin"
    OPENSEARCH_PASSWORD: str = "admin"
    OPENSEARCH_VERIFY_CERTS: bool = False
    OPENSEARCH_USE_SSL: bool = False
    OPENSEARCH_SSL_SHOW_WARN: bool = False   



settings = Config()

fastapi_config: dict[str, Any] = {
    "title": "Inventory API"
}

# No OpenAPI docs in production
if not settings.ENVIRONMENT.is_debug:
    fastapi_config["openapi_url"] = None

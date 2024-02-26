import logging
from typing import AsyncGenerator
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config import fastapi_config

logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(_application: FastAPI) -> AsyncGenerator:
    logger.info("*** Server starting UP ***")
    yield

    # Shutdown
    logger.info("*** Server shutting DOWN ***")


def create_app() -> FastAPI:
    from app.router import router as product_router
    from app.config import settings

    app = FastAPI(**fastapi_config, lifespan=lifespan)

    app.include_router(product_router, tags=["Products"])

    return app

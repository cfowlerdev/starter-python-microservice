import logging
import uuid
from opensearchpy import AsyncOpenSearch
from fastapi import APIRouter, status, Depends
from app.db.client import get_osearch_client
from app.schemas.product import ProductResponse
from app.models.product import Product

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get(
        "/{product_id}",
        response_model=ProductResponse,
        status_code = status.HTTP_200_OK,
        description = "Get a product by id",
        summary = "Get a product by id"
)
async def route_get_product_by_id(product_id: uuid.UUID, os_client: AsyncOpenSearch = Depends(get_osearch_client)):
    # TODO: Need to find a way to import OSearch client through FastAPI dependency
    product = await Product.get_by_id(product_id)

    pass
from opensearchpy import AsyncOpenSearch
from app.config import settings

osearch_client = AsyncOpenSearch(
    hosts=[{"host": settings.OPENSEARCH_HOST, "port": settings.OPENSEARCH_PORT}],
    http_compress=True,  # enables gzip compression for request bodies
    # TODO: support OpenSearch auth
    # http_auth=(settings.OPENSEARCH_USERNAME, settings.OPENSEARCH_PASSWORD),
    use_ssl=settings.OPENSEARCH_USE_SSL,
    verify_certs=settings.OPENSEARCH_VERIFY_CERTS,
    ssl_show_warn=settings.OPENSEARCH_SSL_SHOW_WARN,
)

async def get_osearch_client() -> AsyncOpenSearch:
    return osearch_client


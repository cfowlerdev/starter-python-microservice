from app.models import base
from opensearch_dsl import Text, Keyword, Double, Boolean

class Product(base.BaseDocument):
    name: Text()
    description: Text()
    price: Double()
    category: Keyword()
    tags: Keyword()
    brand: Keyword()
    availability: Boolean()

    class Index:
        """
        Defines the index to use
        """
        # TODO: Make it configurable
        name = "products"
        settings = {
            "refresh_interval": "1s"
        }
    

    

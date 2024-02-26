import uuid
import datetime
from opensearch_dsl import Document, Keyword, Date

class BaseDocument(Document):

    uuid = Keyword()
    created_at = Date()
    updated_at = Date()
    # TODO: could add user details here? who created, who updated
    # created_by
    # updated_by

    @classmethod
    def search(cls, using):
        pass
        # https://github.com/reflexsoar/reflex-api/blob/4b7270958b013a579fe885d2ebf8fbf68db11d2b/app/api_v2/model/base.py#L73
        # How it's used:
        

        # TODO:
        # Look at this : https://github.com/reflexsoar/reflex-api/blob/4b7270958b013a579fe885d2ebf8fbf68db11d2b/app/api_v2/model/base.py#L73
        # Could we simply do the dependency on the OS client in the document instead?
        # Look at the "search" classmethod. Would be cool to do something like that but use dependency to get connection

    @classmethod
    async def get_by_id(cls, uuid, all_results: bool = False, **kwargs):
        """
        Fetches a document matching the given UUID
        """
        response = cls.search()
        response = await response.query('term', uuid=uuid, **kwargs).execute()
        if response:
            return response[0]
        return None

    async def save(self, **kwargs):
        """
        Overrides the default save function to ensure base fields are stored
        """
        if not self.created_at:
            self.created_at = datetime.datetime.utcnow()
        if not self.updated_at:
            self.updated_at = self.created_at
        if not self.uuid:
            self.uuid = uuid.uuid4()
        return super().save(**kwargs)

    async def update(self, **kwargs):
        """
        Overrides the default update function to ensure base fields are updated
        """
        self.updated_at = datetime.datetime.utcnow()
        return super().update(**kwargs)


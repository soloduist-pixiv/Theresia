from datetime import datetime, timezone
from uuid import uuid4

from elasticsearch import Elasticsearch

from app.core.config import settings
from app.schemas.article import ArticleCreateRequest


class ArticleService:
    def __init__(self) -> None:
        self.client = Elasticsearch(settings.elasticsearch_url)
        self.index = settings.elasticsearch_index

    def create_article(self, payload: ArticleCreateRequest) -> str:
        article_id = str(uuid4())
        body = {
            "title": payload.title,
            "content": payload.content,
            "tags": payload.tags,
            "created_at": datetime.now(timezone.utc).isoformat(),
        }
        self.client.index(index=self.index, id=article_id, document=body, refresh=True)
        return article_id

    def list_articles(self) -> list[dict]:
        result = self.client.search(
            index=self.index,
            query={"match_all": {}},
            sort=[{"created_at": {"order": "desc"}}],
            size=60,
        )
        return [{"id": hit["_id"], **hit["_source"]} for hit in result["hits"]["hits"]]

    def get_article(self, article_id: str) -> dict | None:
        if not self.client.exists(index=self.index, id=article_id):
            return None
        result = self.client.get(index=self.index, id=article_id)
        return {"id": result["_id"], **result["_source"]}

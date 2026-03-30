from fastapi import APIRouter, HTTPException, status

from app.core.response import json_response
from app.schemas.article import ArticleCreateRequest
from app.services.article_service import ArticleService

router = APIRouter(prefix="/article", tags=["article"])
article_service = ArticleService()


@router.post("")
async def create_article(payload: ArticleCreateRequest):
    article_id = article_service.create_article(payload)
    return json_response(
        status_code=status.HTTP_201_CREATED,
        message="文章创建成功",
        data={"id": article_id},
    )


@router.get("")
async def list_articles():
    articles = article_service.list_articles()
    return json_response(status_code=status.HTTP_200_OK, message="ok", data=articles)


@router.get("/{article_id}")
async def get_article(article_id: str):
    article = article_service.get_article(article_id)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="文章不存在")
    return json_response(status_code=status.HTTP_200_OK, message="ok", data=article)

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.article import router as article_router
from app.api.chat import router as chat_router
from app.api.login import router as login_router
from app.api.register import router as register_router
from app.core.database import Base, engine


@asynccontextmanager
async def lifespan(_: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title="MyProject", lifespan=lifespan)
app.include_router(login_router)
app.include_router(register_router)
app.include_router(chat_router)
app.include_router(article_router)

from datetime import datetime, timezone

from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.response import json_response
from app.core.security import verify_password
from app.models.user import UserModel
from app.schemas.auth import LoginRequest

router = APIRouter()


@router.post("/login")
async def login(user: LoginRequest, db: AsyncSession = Depends(get_db)):
    db_user = await db.scalar(select(UserModel).where(UserModel.username == user.username))
    if not db_user or not verify_password(user.password, db_user.password):
        return json_response(
            status_code=status.HTTP_401_UNAUTHORIZED,
            message="用户名或密码错误",
        )

    db_user.last_login_at = datetime.now(timezone.utc)
    await db.commit()

    return json_response(
        status_code=status.HTTP_200_OK,
        message="登录成功",
        data={"id": db_user.id, "username": db_user.username},
    )

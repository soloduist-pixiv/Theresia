from fastapi import APIRouter, Depends, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.database import get_db
from app.core.response import json_response
from app.core.security import hash_password
from app.models.user import UserModel
from app.schemas.auth import RegisterRequest

router = APIRouter()


@router.post("/register")
async def register(user: RegisterRequest, db: AsyncSession = Depends(get_db)):
    db_user = await db.scalar(select(UserModel).where(UserModel.username == user.username))
    if db_user:
        return json_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            message="用户名已存在",
        )

    new_user = UserModel(username=user.username, password=hash_password(user.password))
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return json_response(
        status_code=status.HTTP_201_CREATED,
        message="注册成功",
        data={"id": new_user.id, "username": new_user.username},
    )

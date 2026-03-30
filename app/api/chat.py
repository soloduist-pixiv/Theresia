from fastapi import APIRouter, status

from app.core.response import json_response
from app.schemas.chat import ChatRequest
from app.services.chat_service import ChatService

router = APIRouter()
chat_service = ChatService()


@router.post("/chat")
async def chat(payload: ChatRequest):
    try:
        answer = chat_service.chat(payload.prompt)
        return json_response(status_code=status.HTTP_200_OK, message="ok", data={"answer": answer})
    except ValueError as error:
        return json_response(
            status_code=status.HTTP_400_BAD_REQUEST,
            message=str(error),
            data={"answer": ""},
        )

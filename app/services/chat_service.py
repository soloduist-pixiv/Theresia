from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

from app.core.config import settings


class ChatService:
    def __init__(self) -> None:
        self.model = None
        if settings.openai_api_key:
            self.model = ChatOpenAI(
                model=settings.openai_model,
                api_key=settings.openai_api_key,
                base_url=settings.openai_base_url,
                temperature=0.7,
            )
        self.parser = StrOutputParser()

    def chat(self, prompt: str) -> str:
        if self.model is None:
            raise ValueError("OPENAI_API_KEY 未配置")
        chat_message = [
            SystemMessage(content="你是一个专业的博客助手"),
            HumanMessage(content=prompt),
        ]
        result = self.model.invoke(chat_message)
        return self.parser.invoke(result)

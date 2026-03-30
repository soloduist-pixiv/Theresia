import langchain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_core.tools import BaseTool
from core.config import Settings
from langchain_core.output_parsers import StrOutputParser

class ChatTool:
    def __init__(self):
        self.api_key = Settings.DeepSeek_API_Key
        self.model = ChatOpenAI(
            model="deepseek-chat",
            base_url="https://api.deepseek.com/v1",
            api_key=self.api_key,
            max_tokens=8192,
            temperature=0.7,
        )
        self.parser = StrOutputParser()
    
    def chat(self, prompt:str):
        chat_message = [
            SystemMessage(content="你是一个专业的助手"),
            HumanMessage(content=prompt),
        ]
        result = self.model.invoke(chat_message)
        return self.parser.invoke(result)
             

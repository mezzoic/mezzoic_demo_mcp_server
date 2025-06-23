from abc import ABC, abstractmethod
from starlette.requests import Request
from starlette.responses import PlainTextResponse
from app.domain.user import User

class IToolsController(ABC):
    @abstractmethod
    def sentiment_analysis(self, text: str) -> str:
        ...
    @abstractmethod
    def health_check(self) -> PlainTextResponse:
        ...
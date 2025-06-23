from abc import ABC, abstractmethod
from starlette.responses import PlainTextResponse

class IToolsController(ABC):
    @abstractmethod
    def sentiment_analysis(self, text: str) -> str:
        ...
    @abstractmethod
    def health_check(self) -> PlainTextResponse:
        ...
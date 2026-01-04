from abc import ABC, abstractmethod

from model.execution_request import ExecutionRequest


class GenAiService(ABC):

    @abstractmethod
    def generate_text(self, request: ExecutionRequest) -> str:
        pass
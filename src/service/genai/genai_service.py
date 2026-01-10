from abc import ABC, abstractmethod

from model.execution_request import ExecutionRequest


class GenAiService(ABC):
    """Abstract base class for GenAI services"""

    @abstractmethod
    def generate_text(self, request: ExecutionRequest) -> str:
        """Abstract method to generate text based on the execution request"""
        pass

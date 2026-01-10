from pydantic import BaseModel

from config.ModelEnum import ModelEnum


class ExecutionRequest(BaseModel):
    question: str
    model_enum: ModelEnum
    parameters: dict[str, str] | None = None

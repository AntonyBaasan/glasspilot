from pydantic import BaseModel


class ExecutionRequest(BaseModel):
    command: str
    parameters: dict[str, str] | None = None

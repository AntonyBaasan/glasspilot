from pydantic import BaseModel


class LlmConfig(BaseModel):
    model_name: str
    temperature: float = 0.7
    max_tokens: int = 1500
    top_p: float = 1.0
    frequency_penalty: float = 0.0
    presence_penalty: float = 0.0
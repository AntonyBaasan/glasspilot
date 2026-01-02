import os

from config.ModelEnum import ModelEnum
from model.execution_request import ExecutionRequest
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")


class ExecutorService:
    def execute(self, request: ExecutionRequest) -> str:
        if request.model_enum == ModelEnum.GEMINI_3_FLASH_PREVIEW:
            client = genai.Client(api_key=gemini_api_key)
            response = client.models.generate_content(
                model=ModelEnum.GEMINI_3_FLASH_PREVIEW.value,
                contents=[
                    types.Content(
                        role="user",
                        parts=[
                            types.Part.from_text(text=request.command)
                        ]
                    )
                ],
                config=types.GenerateContentConfig(
                    thinking_config=types.ThinkingConfig(
                        thinking_level="HIGH",
                    ),
                    tools=[],
                )
            )
            return response.text

        # Placeholder for executing a command
        return f"Executing command: {request.command}, using model: {request.model_enum}"


# Singleton instance
executor_service = ExecutorService()

import os

from dotenv import load_dotenv

from config.ModelEnum import ModelEnum
from model.execution_request import ExecutionRequest
from service.genai.genai_service import GenAiService

from google import genai
from google.genai import types

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")

class GeminiService(GenAiService):
    def generate_text(self, request: ExecutionRequest) -> str:
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
        # Implementation for Gemini model text generation
        return f"Generated text for prompt: {prompt} using Gemini model"

gemini_service = GeminiService()
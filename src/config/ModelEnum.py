from enum import Enum


class ModelEnum(str, Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_4 = "gpt-4"
    # gemini models
    GEMINI_3_FLASH_PREVIEW = "gemini-3-flash-preview"
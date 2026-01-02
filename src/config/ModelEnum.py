from enum import Enum


class ModelEnum(str, Enum):
    # gpt 5 models
    GPT_5_2_PRO = "gpt-5.2-pro"
    # gpt 4 models
    GPT_4_1 = "gpt-4.1"
    GPT_4_1_MINI = "gpt-4.1-mini"
    GPT_4o = "gpt-4o"
    GPT_4o_MINI = "gpt-4o-mini"
    # gemini 3 models
    GEMINI_3_PRO_PREVIEW = "gemini-3-pro-preview"
    GEMINI_3_FLASH_PREVIEW = "gemini-3-flash-preview"
    # gemini 2.5 models
    GEMINI_2_5_PRO = "gemini-2.5-pro"
    GEMINI_2_5_FLASH = "gemini-2.5-flash"
    GEMINI_2_5_FLASH_LITE = "gemini-2.5-flash-lite"
    # claude models
    CLAUDE_SONNET_4_5 = "claude-sonnet-4-5"
    CLAUDE_HAIKU_4_5 = "claude-haiku-4-5"

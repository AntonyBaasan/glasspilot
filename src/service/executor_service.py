from config.ModelEnum import ModelEnum
from model.execution_request import ExecutionRequest

from service.genai.gemini_service import gemini_service


class ExecutorService:

    def __init__(self):
        # Create list of supported genai services
        self.init_genai_services()

    def init_genai_services(self):
        self.supported_genai_services = {
            ModelEnum.GEMINI_3_FLASH_PREVIEW: gemini_service,
        }

    def get_genai_service(self, model_enum: ModelEnum):
        return self.supported_genai_services.get(model_enum, None)

    def execute(self, request: ExecutionRequest) -> str:
        gen_service = self.supported_genai_services.get(request.model_enum)

        if gen_service:
            return gen_service.generate_text(request)

        return f"Model {request.model_enum} not supported."


# Singleton instance
executor_service = ExecutorService()

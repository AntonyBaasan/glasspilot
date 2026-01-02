from model.execution_request import ExecutionRequest


class ExecutorService:
    def execute(self, request: ExecutionRequest) -> str:
        # Placeholder for executing a command
        return f"Executing command: {request.command}"

# Singleton instance
executor_service = ExecutorService()
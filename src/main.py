# This is a sample Python script.
import typer

from service.executor_service import executor_service
from model.execution_request import ExecutionRequest

app = typer.Typer()

@app.command()
def execute(command: str):
    request = ExecutionRequest(command=command)
    result = executor_service.execute(request)
    print(result)

@app.command()
def echo(text: str):
    print(f"Echo result: {text}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

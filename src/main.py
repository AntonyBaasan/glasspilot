# This is a sample Python script.

import typer
from rich import print

from config.ModelEnum import ModelEnum
from service.fs.document_service import document_service
from service.embedding.embedding_service import embedding_service
from service.executor_service import executor_service
from model.execution_request import ExecutionRequest

app = typer.Typer()


@app.command()
def execute(question: str):
    """Execute a question using the GenAI executor service."""
    request = ExecutionRequest(
        question=question,
        model_enum=ModelEnum.GEMINI_3_FLASH_PREVIEW
    )
    result = executor_service.execute(request)
    print(result)


@app.command()
def echo(text: str):
    """Echo the provided text."""
    print(f"Echo result: {text}")


@app.command()
def embed(directory: str, file_name: str):
    """Embed documents from the specified path."""

    print(f"Embedding documents from dir: {directory} with files: {file_name}")
    files = []
    # step 1 - load documents from path
    if directory:
        files = document_service.load_files_by_folder(directory)

    if file_name:
        file = document_service.load_files_by_names(file_name)
        if file:
            files.append(file)

    print(f"Loaded files: {files}")

    # step 2 - split documents into chunks
    for file_metadata in files:
        embedding_service.embed_file(file_metadata)

    # step 3 - create embeddings for each chunk
    # step 4 - store embeddings in vector database

    files = []


@app.command()
def search(text: str):
    # step 1 - create embedding for the input text
    # step 2 - search vector database for similar embeddings
    print(f"Searching embedded documents for text: {text}")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

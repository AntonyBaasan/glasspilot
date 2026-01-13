from pydantic import BaseModel


class FileMetadata(BaseModel):
    path: str
    file_name: str

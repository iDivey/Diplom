from pydantic import BaseModel

class BookCreate(BaseModel):
    author: str
    name_father_Author: str
    title: str
    publisher: str
    city: str
    year: int
    pages: int
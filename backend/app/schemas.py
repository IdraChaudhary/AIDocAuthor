from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'

class SectionCreate(BaseModel):
    title: str
    order: int = 0

class ProjectCreate(BaseModel):
    title: str
    doc_type: str = 'docx'
    sections: Optional[List[SectionCreate]] = []

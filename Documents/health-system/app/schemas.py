from pydantic import BaseModel
from typing import List

class ProgramBase(BaseModel):
    name: str

class ProgramCreate(ProgramBase): pass
class Program(ProgramBase):
    id: int
    class Config:
        from_attributes = True  # Change from orm_mode to from_attributes

class ClientBase(BaseModel):
    name: str
    age: int
    contact: str

class ClientCreate(ClientBase): pass
class Client(ClientBase):
    id: int
    class Config:
        from_attributes = True  # Change from orm_mode to from_attributes

class ClientProfile(Client):
    programs: List[Program]

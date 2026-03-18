from pydantic import BaseModel

class WaitList(BaseModel):
    name:str
    email:str
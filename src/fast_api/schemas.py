from pydantic import BaseModel


class Messagem(BaseModel):
    message: str

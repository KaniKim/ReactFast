from pydantic import BaseModel


class AcessToken(BaseModel):
    token: str
    token_type: str
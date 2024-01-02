from pydantic import BaseModel, Field


class UserToken(BaseModel):
    id: str = Field(example="{uuid}")
    email: str = Field(None, example="example@email.com")
    status: str = Field(None, example=True)

    class Config:
        orm_mode = True
class ProfileInfo(BaseModel):
    id: str = Field(example="{uuid}")
    user_id: str = Field(None, nullable=False, example="{uuid}")
    picture_url: str = Field(None, example="https://picture.png")
    nick_name: str = Field(None, nullable=True, example="kani")

    class Config:
        orm_mode = True
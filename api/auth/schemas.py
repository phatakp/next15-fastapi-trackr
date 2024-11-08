from pydantic import BaseModel


class GoogleUser(BaseModel):
    sub: int
    email: str
    name: str
    picture: str | None


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str


class RefreshTokenRequest(BaseModel):
    refresh_token: str


class AccessTokenRequest(BaseModel):
    access_token: str

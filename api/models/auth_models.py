import uuid
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, SQLModel


class User(SQLModel, table=True):
    __tablename__ = "users"

    id: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False,
                         primary_key=True, default=uuid.uuid4)
    )
    email: str = Field(unique=True)
    google_sub: str = Field(unique=True, nullable=True)
    name: str
    picture: str | None = Field(None, nullable=True)
    is_verified: bool = Field(default=False)
    created_at: datetime = Field(sa_column=Column(
        pg.TIMESTAMP, default=datetime.now))
    update_at: datetime = Field(sa_column=Column(
        pg.TIMESTAMP, default=datetime.now))

    def __repr__(self):
        return f"<User {self.name}>"

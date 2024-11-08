import uuid
from enum import StrEnum
import sqlalchemy.dialects.postgresql as pg
from sqlmodel import Column, Field, SQLModel, UniqueConstraint


class AcctType(StrEnum):
    SAVINGS = "savings"
    CREDITCARD = "credit_card"
    MORTGAGE = "mortgage"
    WALLET = "wallet"
    INVESTMENT = "investment"


class Bank(SQLModel, table=True):
    __tablename__ = "banks"

    id: uuid.UUID = Field(
        sa_column=Column(pg.UUID, nullable=False,
                         primary_key=True, default=uuid.uuid4)
    )
    name: str
    type: AcctType = Field(sa_column=Column(
        pg.ENUM(AcctType), nullable=False))

    __table_args__ = (UniqueConstraint(
        "name", "type", name="bank_unique_constraint"),)

    def __repr__(self):
        return f"<Bank {self.name}-{self.type}>"

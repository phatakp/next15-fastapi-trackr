from pydantic import BaseModel, ConfigDict
import uuid
from api.models import AcctType


class BankCreateSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str
    type: AcctType


class BankSchema(BankCreateSchema):
    id: uuid.UUID

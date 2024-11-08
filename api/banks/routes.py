from fastapi import APIRouter
from typing import List
from .services import BankService
from .schema import BankCreateSchema, BankSchema
from api.core.db import db_dependency
from api.errors import BankNotFound


bank_router = APIRouter()
bank_service = BankService()


@bank_router.get("", response_model=List[BankSchema])
async def all_banks(session: db_dependency):
    banks = await bank_service.get_all_banks(session=session)
    return banks


@bank_router.get("/{bank_id}", response_model=BankSchema)
async def get_bank(bank_id: str, session: db_dependency):
    bank = await bank_service.get_bank_by_id(id=bank_id, session=session)
    if bank:
        return bank
    raise BankNotFound()


@bank_router.post("")
async def add_bank(bank_data: BankCreateSchema, session: db_dependency):
    bank = await bank_service.create_bank(bank_data=bank_data, session=session)
    return bank

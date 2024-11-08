from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import asc, select
from api.models import Bank
from .schema import BankCreateSchema


class BankService:
    async def get_all_banks(self, session: AsyncSession):
        statement = select(Bank).order_by(asc(Bank.type))
        result = await session.exec(statement)
        return result.all()

    async def get_bank_by_id(self, id: str, session: AsyncSession):
        statement = select(Bank).where(Bank.id == id)
        result = await session.exec(statement)
        bank = result.first()
        return bank if bank else None

    async def create_bank(self, bank_data: BankCreateSchema, session: AsyncSession):
        bank_data_dict = bank_data.model_dump()
        new_bank = Bank(**bank_data_dict)
        session.add(new_bank)
        await session.commit()
        return new_bank

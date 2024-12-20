from sqlalchemy import BigInteger 
from sqlalchemy.orm import Mapped,mapped_column,DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncAttrs
from config import SQLALCHEMY_URL

engine = create_async_engine(SQLALCHEMY_URL,echo=True)

async_session = async_sessionmaker(engine,expire_on_commit=False)

class Base(AsyncAttrs,DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)
    question:  Mapped[str] = mapped_column()
    answer: Mapped[str] = mapped_column()


async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.pool import NullPool
from sqlalchemy.sql import text

from alembic_db.db_schema import Data

load_dotenv()

engine = create_async_engine(
    f"postgresql+asyncpg://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}",
    pool_pre_ping=True,
    poolclass=NullPool,
)

session = AsyncSession(engine)


async def insert():
    async with session:
        session.add(Data(id=1, data_value=100.1231231313))
        await session.commit()


async def insert_raw():
    async with session:
        await session.execute(text("insert into data_table values(2, 100.1231231313)"))
        await session.commit()


if __name__ == "__main__":
    import asyncio

    # asyncio.run(insert_raw())
    asyncio.run(insert())

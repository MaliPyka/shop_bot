import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# Используем 127.0.0.1 вместо localhost — это надежнее для Windows

DB_URL = os.getenv(
    "DB_URL",
    "postgresql+asyncpg://user:password@127.0.0.1:5432/shop_database"
)


engine = create_async_engine(
    DB_URL,
    echo=True,
    # Эти параметры помогают, если соединение обрывается
    pool_pre_ping=True,
    connect_args={
        "command_timeout": 60,
    }
)

async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass
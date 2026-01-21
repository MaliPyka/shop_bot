from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase


DB_URL = "postgresql+asyncpg://postgres:2323@localhost:5432/appdb"


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
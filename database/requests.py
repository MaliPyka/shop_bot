from aiogram.types import Update

from database.models import User
from database.engine import async_session
from database.models import Product
from database.models import Category

from sqlalchemy import select, update


async def set_user(tg_id, username, first_name):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.tg_id == tg_id))

        if not user:
            session.add(User(tg_id=tg_id, username=username, first_name=first_name))
            await session.commit()


async def get_product_id(product_id):
    async with async_session() as session:
        return await session.scalar(select(Product).where(Product.id == product_id))


async def get_categories():
    async with async_session() as session:
        result =  await session.scalars(select(Category))
        return result.all()


async def get_product_by_category(category_id):
    async with async_session() as session:
        result = await session.scalars(select(Product).where(Category.id == category_id))
        return result.all()


async def get_admins():
    async with async_session() as session:
        result = await session.scalars(select(User.tg_id).where(User.is_admin == True))
        return set(result.all())


async def set_admin(tg_id):
    async with async_session() as session:
        await session.execute(update(User).where(User.tg_id == tg_id).values(is_admin=True))
        await session.commit()

async def add_category(category_name):
    async with async_session() as session:
        session.add(Category(name=category_name))
        await session.commit()

async def get_categories_name():
    async with async_session() as session:
        result = await session.scalars(select(Category.name))
        return set(result.all())
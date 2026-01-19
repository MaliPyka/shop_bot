from database.models import User
from database.engine import async_session
from database.models import Product
from database.models import Category

from sqlalchemy import select


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

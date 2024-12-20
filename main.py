import asyncio

import logging 
import sys

from aiogram import Bot, Dispatcher,  types
from aiogram.filters import Command, CommandStart
from aiogram.types import Message

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

from sqlalchemy import Select as select

from models import async_main,User,async_session

from kb import *

from config import bot_token,ai_token


bot = Bot(bot_token)
dp = Dispatcher()

model = GigaChat(
    credentials=ai_token,
    scope="GIGACHAT_API_PERS",
    model="GigaChat",
    role = "assistant",
    stream =  True,
    verify_ssl_certs=False,
    
)

messages = [
    SystemMessage(
        content="Ты бот, ты пытаешься помочь подробно разобраться в задаваемых вопросах"
    )
]

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Helo,im your AI assistant",reply_markup=keyboard)

@dp.message(Command("clear"))
async def cmd_clear(message: types.Message):
    async with async_session() as session:
        async with session.begin():
            res = await session.execute(select(User).where(User.tg_id == message.from_user.id))
            results = res.scalars().all()
            for i in results:
                 await session.delete(i)
            await session.flush()
        await message.answer("очищено")

@dp.message()
async def answ(message: Message):
    messages.append(HumanMessage(content=message.text))
    res = model.invoke(messages)
    messages.append(res)

    user = User(
        tg_id = message.from_user.id,
        question = message.text,
        answer = res.content
            )

    async with async_session() as session:
            session.add(user)
            await session.commit()
            await session.flush()
    await message.answer(res.content)

        
async def main():
    await async_main()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)
    asyncio.run(main())
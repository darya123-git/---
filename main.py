import asyncio
import logging
from config import *
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command


API_TOKEN = TOKEN

# Включаем логирование, чтобы видеть сообщения в консоли
logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher()


#Хэндлер на команду /start
@dp.message(Command("start"))
async def command_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Массажные услуги")],
        [types.KeyboardButton(text="Уход за кожей лица")],
        [types.KeyboardButton(text="Услуги для рук и ног")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer('Здравствуйте! Добро пожаловать в наш салон "Здоровье и красота". Запишитесь на процедуру и мы уверены, что вы останетесь довольны!', reply_markup=keyboard)


#Хэндлер на сообщения
@dp.message(F.text)
async def msg_echo(message: types.Message):
    msg_user = message.text.lower()
    name = message. chat.first_name
    if "привет" in msg_user:
        await message.answer(f"Привет, {name}!")
    elif "пока" in msg_user:
        await message.answer(f"пока, {name}!")
    elif "ты кто" in msg_user:
        await message.answer(f"Я БОТ, {name}!")
    elif "массажные услуги" in msg_user:
        await message.answer("- Общий оздоровительный\n- Антицеллюлитный\n- Точечный")
    elif "уход за кожей лица" in msg_user:
        await message.answer("- Чистка лица\n- Химические пилинги\n- Массаж | Маски")
    elif "услуги для рук и ног" in msg_user:
        await message.answer("- Парафинотерапия")


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
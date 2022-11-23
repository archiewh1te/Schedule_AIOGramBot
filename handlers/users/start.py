from aiogram import types
from filters import IsPrivate
from loader import dp
from utils.misc import rate_limit
from SQL.sqlite_request import output


# Функция по команде /start
@rate_limit(limit=3)
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    await message.answer(f"Привет {message.from_user.first_name} 🤚"
                         f"Я бот - Планировщик событий")


@dp.message_handler(text='/schedule')
async def start_schedule(message: types.Message):  # Вывод списка из фаила  SQL.PY
    await message.answer('Напоминание уже запущено')
    await message.answer(f'{output}')




from loader import dp, bot
from data.config import channel_id
from SQL.sqlite_request import output
import aioschedule
import asyncio


# Функция которая отправляет в группу данные из БД
async def send_schedule():
    await bot.send_message(channel_id,
                     f' Список напоминаний:\n' + output)


# Ставим время когда бот будет писать в группу 1 раз в день
async def scheduler():
    aioschedule.every().day.at("16:43").do(send_schedule)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)
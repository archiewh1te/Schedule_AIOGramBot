async def on_startup(dp):

    # Подключение планировщика
    import asyncio
    from handlers.users import scheduler
    asyncio.create_task(scheduler())

    # Подключение мидлвар и фильтр
    import middlewares
    middlewares.setup(dp)

    import filters
    filters.setup(dp)


    # Подключение уведомление админам о запуске
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)


    # Подключение команд бота
    from utils.set_bot_commands import set_default_commands
    await set_default_commands(dp)
    print('Бот запущен')


if __name__ == '__main__':
    from aiogram import executor
    from handlers import dp



    executor.start_polling(dp, on_startup=on_startup, skip_updates=False)

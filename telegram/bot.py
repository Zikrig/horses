import asyncio
from aiogram import Bot, Dispatcher
from handlers.person import register, del_me, gimme, give_me_horse
from handlers import start, web


# Запуск бота
async def main():
    bot = Bot(token="")
    dp = Dispatcher()

    dp.include_routers(register.router, del_me.router, gimme.router, give_me_horse.router, start.router, web.router)

    # Альтернативный вариант регистрации роутеров по одному на строку
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
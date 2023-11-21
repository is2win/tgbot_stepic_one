import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

# Функция конфигурирования и запуска бота
async def main() -> None:

    # Загружаем конфиг во временную переменную
    config: Config = load_config()

    # Инициализируем бот и диспетчер
    bot = Bot(token=config.tg_bot.token)
    dp = Dispatcher()

    # пропускаем накопившиеся апдейты и запускаем pooling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_pooling(bot)

if __name__ == '__main__':
    asyncio.run(main())

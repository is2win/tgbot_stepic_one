from aiogram.types import Message
from aiograms.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU

# Хэндлер на команду /start
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])

# Хэндлер на команду /help
@dp.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

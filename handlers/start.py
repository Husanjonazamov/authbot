# aiogram import
from aiogram.types import Message
from aiogram.dispatcher import FSMContext

# kode import
from loader import dp
from utils import texts, buttons
from utils.state import Register



@dp.message_handler(commands=['start'], state='*')
async def start_handlers(message: Message, state: FSMContext):
    """
    /start 
    """
    await message.answer(texts.START_HANDLER)
    await Register.name.set()
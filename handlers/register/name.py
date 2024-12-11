from aiogram.types import Message
from aiogram.dispatcher import FSMContext

from utils import texts, buttons
from loader import dp, bot
from utils.state import Register




@dp.message_handler(content_types=['text'], state=Register.name)
async def name_handler(message: Message, state: FSMContext):
    name = message.text
    
    await state.update_data({
        'name': name
    })
    
    await message.answer(texts.PHONE, reply_markup=buttons.PHONE)
    await Register.phone.set()






from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp, bot
from utils import texts, buttons
from utils.state import Register
from utils.env import REGISTER_URL
from services.services import CreateUser, getUser

import random



@dp.message_handler(content_types=['contact'], state=Register.phone)
async def phone_handler(message: Message, state: FSMContext):
    phone = message.contact.phone_number
    user_id = message.from_user.id
    
    data = await state.get_data()
    name = data.get('name')
    
    random_code = random.randint(100000, 999999)
    user = getUser(user_id)

    if user:
        await message.answer(texts.LOGIN_RETURN)
    else:
        user = {
            'user_id': user_id,
            'name': name,
            "phone": phone,
            "random_code": random_code,
            "is_verified": False
        }
        response = await CreateUser(user)
        
        
        if response:    
            url = f'{REGISTER_URL}/verify?user_id={user_id}&code={random_code}'
            await message.answer(texts.SUCCESS.format(random_code), reply_markup=buttons.return_url(url))
        else:
            await message.answer("Xatolik yuz berdi. Iltimos, keyinroq urinib ko'ring.")

from aiogram.types import Message
from aiogram.dispatcher import FSMContext
from loader import dp
from utils import texts, buttons
from services.services import getUser
from utils.env import REGISTER_URL



@dp.message_handler(commands=['login'], state='*')
async def phone_handler(message: Message, state: FSMContext):
    user_id = message.from_user.id
    user = getUser(user_id)
    login_code = user['random_code']

    if user:
        LOGIN_URL = f'{REGISTER_URL}/verify?user_id={user_id}&code={login_code}'
        await message.answer(texts.LOGIN_SUCCESS.format(login_code), reply_markup=buttons.login_url(LOGIN_URL))
   
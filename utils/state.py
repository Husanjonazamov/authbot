from aiogram.dispatcher.filters.state import State, StatesGroup



class Register(StatesGroup):
    name = State()
    phone = State()
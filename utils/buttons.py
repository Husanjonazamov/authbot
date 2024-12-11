from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton




PHONE = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Telefon raqamni yuborish', request_contact=True)
        ]
    ],
    resize_keyboard=True
)

def return_url(url):
    markub = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="✅ Ro'yhatdan o'tdim", url=url)
    
    markub.add(button)
    
    return markub
    
    
    
def login_url(url):
    markub = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="✅ Kirish", url=url)
    
    markub.add(button)
    
    return markub
    
    
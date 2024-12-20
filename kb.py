from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb_list = [
    [KeyboardButton(text="/clear")]
]

keyboard = ReplyKeyboardMarkup(keyboard=kb_list, resize_keyboard=True, one_time_keyboard=True)
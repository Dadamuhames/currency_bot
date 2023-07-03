from loader import dp
from cache import _cache
from user_session import UserSession
from aiogram import types
from keyboards import currencies_keyboard, currencies_simple_keyboard, language_keyboard
import texts


@dp.message_handler(commands=['language'])
async def choose_language(message: types.Message):
    reply_keyboard = language_keyboard()
    await message.answer(texts.choose_language_text, reply_markup=reply_keyboard)



# start hadler
@dp.message_handler(commands=['start'])
async def start(message: types.Message, session: UserSession, session_data: dict):
    lang = session_data.get("language")

    reply_keyboard = currencies_simple_keyboard()

    await message.answer(texts.start_text.get(lang), reply_markup=reply_keyboard)
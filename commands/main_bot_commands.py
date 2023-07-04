from loader import dp
from user_session import UserSession
from aiogram import types
from keyboards import currencies_keyboard, currencies_simple_keyboard, language_keyboard
import texts
from db import User


@dp.message_handler(commands=['language'])
async def choose_language(message: types.Message):
    reply_keyboard = language_keyboard()
    await message.answer(texts.choose_language_text, reply_markup=reply_keyboard)



# start hadler
@dp.message_handler(commands=['start'])
async def start(message: types.Message, session: UserSession, session_data: dict):
    lang = session_data.get("language")

    reply_keyboard = currencies_simple_keyboard(lang)

    await message.answer(texts.start_text.get(lang), reply_markup=reply_keyboard)


# off updates
@dp.message_handler(commands=['updatesOff'])
async def updates_off(message: types.Message, session: UserSession, session_data: dict):
    try:
        user_model = User()
        lang = session_data.get('language')

        user_model.change_updates(message.chat.id, 0)
        
        await message.answer(texts.updates_off.get(lang, ''))
    except Exception as e:
        print("ERROR!", e)


# on updates
@dp.message_handler(commands=['updatesOn'])
async def updates_off(message: types.Message, session: UserSession, session_data: dict):
    try:
        user_model = User()
        lang = session_data.get('language')

        user_model.change_updates(message.chat.id, 1)

        await message.answer(texts.updates_on.get(lang, ''))
    except Exception as e:
        print("ERROR!", e)

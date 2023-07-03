from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from filters import *
from keyboards import *
from cache import _cache
from user_session import UserSession
from utils import *
import texts


# all currencies
@dp.message_handler(Text(equals="Все валюты🌐"))
async def all_currencies(message: types.Message, session: UserSession, session_data: dict):
    currencies = await get_all_currs()
    reply_markup = currencies_keyboard(currencies)

    text = texts.choose_curr.get(session_data.get("language"))

    await message.answer(text, reply_markup=reply_markup)



# saved
@dp.message_handler(Text(equals="Избранные💾"))
async def saved(message: types.Message, session: UserSession, session_data: dict):
    curency_codes = session_data.get("currencies", [])
    curencies = await get_currencies_from_list(curency_codes)
    lang = session_data.get("language")


    if len(curencies):
        for data in curencies:
            reply_keyboard = save_keyboard(saved=True, cur=data.get('Ccy'))

            text = texts.currency_text(lang, data)

            await message.answer(text=text, reply_markup=reply_keyboard)

    else:
        reply_keyboard = simple_keyboard()

        text = texts.there_is_no_saved.get(lang)
        await message.answer(text=text, reply_markup=reply_keyboard)



# currency message handler
@dp.message_handler(currency_filter)
async def currency_info(message: types.Message, session: UserSession, session_data: dict):
    code = message.text[:-2]
    lang = session_data.get("language")

    currency = await get_currency(code)

    if currency is None:
        text = texts.there_is_no_info.get(lang)
        reply_keyboard = currencies_simple_keyboard()

        await message.answer(text, reply_markup=reply_keyboard)

    else:
        text = texts.currency_text(lang, currency)

        code = currency.get('Ccy')
        saved = code in session_data.get('currencies', [])


        reply_keyboard = save_keyboard(saved, code)

        await message.answer(text=text, reply_markup=reply_keyboard)


        
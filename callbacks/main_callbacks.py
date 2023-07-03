from filters import QueryFilter
from aiogram import types
from cache import _cache
from user_session import UserSession
from loader import dp, bot
import json
from keyboards import currencies_simple_keyboard, save_keyboard
import texts


# choose language
@dp.callback_query_handler(QueryFilter("choose_lang"))
async def choose_language(call: types.CallbackQuery, session: UserSession, session_data: dict):
    call_data = json.loads(call.data)
    lang = call_data.get('lang')
    session.set_language(lang)

    print(session.get_or_create())

    await bot.send_message(chat_id=call.from_user.id, text=texts.start_text.get(lang), reply_markup=currencies_simple_keyboard())



# save currency
@dp.callback_query_handler(QueryFilter("save_currency"))
async def save_or_delete_curransy(call: types.CallbackQuery, session: UserSession, session_data: dict):
    call_data = json.loads(call.data)
    
    currency = call_data.get("currency")

    saved = session.add_or_delete(currency)

    reply_keyboard = save_keyboard(saved, currency)

    await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=reply_keyboard)

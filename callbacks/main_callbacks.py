from filters import QueryFilter
from aiogram import types
from user_session import UserSession
from loader import dp, bot
import json
from keyboards import currencies_simple_keyboard, save_keyboard
import texts


# choose language
@dp.callback_query_handler(QueryFilter("choose_lang"))
async def choose_language(call: types.CallbackQuery, session: UserSession, session_data: dict):
    old_lang = session.get_or_create().get("language")
    call_data = json.loads(call.data)
    lang = call_data.get('lang')
    session.set_language(lang)

    print(call.from_user)

    text = ''
    if not old_lang:
        text = texts.start_text.get(lang, '')
    else:
        text = texts.language_updated.get(lang, '')
        
    await bot.send_message(chat_id=call.from_user.id, text=text, reply_markup=currencies_simple_keyboard(lang))



# save currency
@dp.callback_query_handler(QueryFilter("save_currency"))
async def save_or_delete_curransy(call: types.CallbackQuery, session: UserSession, session_data: dict):
    call_data = json.loads(call.data)
    lang = session_data.get('language', '')
    
    currency = call_data.get("currency")

    try:
        saved = session.add_or_delete(currency)

        if saved:

            reply_keyboard = save_keyboard(saved, currency)

            await bot.edit_message_reply_markup(chat_id=call.from_user.id, message_id=call.message.message_id, reply_markup=reply_keyboard)

        else:
            await bot.delete_message(chat_id=call.from_user.id, message_id=call.message.message_id)

    except:
        await bot.send_message(call.from_user.id, text=texts.error_text.get(lang))
        

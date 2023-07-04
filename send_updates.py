from db import mycursor, User
from user_session import UserSession
from utils import get_currencies_from_list
from loader import bot
import texts
from keyboards import save_keyboard
from aiogram.utils.exceptions import ChatNotFound
from aiogram import md
users_model = User()

# send message
async def send_saved_currensy(chat_id, data, lang):
    try:
        reply_keyboard = save_keyboard(saved=True, cur=data.get('Ccy'))

        text = texts.currency_text(lang, data)

        await bot.send_message(chat_id=chat_id, text=text, reply_markup=reply_keyboard)
    except ChatNotFound:
        try:
            users_model.delete_user(chat_id)
        except Exception as e:
            print("ERROR!", e)

    except Exception as e:
        print("ERROR!", e)


# broadcast to users
async def broadcast_saveds():
    try:
        users = users_model.get_updatable_users()

        for user in users:
            chat_id = user[0]

            session = UserSession(mycursor, chat_id)    
            lang = session.get_or_create().get('language', '')        

            codes = session.get_currencies()

            currencies = await get_currencies_from_list(codes)


            if len(currencies):
                await bot.send_message(chat_id=chat_id, text=texts.there_is_updates.get(lang))

            for data in currencies:
                await send_saved_currensy(chat_id, data, lang)

    except Exception as e:
        print("ERROR!", e)
        raise e


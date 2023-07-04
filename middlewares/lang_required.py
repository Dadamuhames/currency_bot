from aiogram.dispatcher.middlewares import BaseMiddleware
from user_session import UserSession
from aiogram import types
from keyboards import language_keyboard
import texts
from loader import bot
from aiogram.dispatcher.handler import CancelHandler, current_handler
from db import mycursor
import json


# lang required
class LanguageRequired(BaseMiddleware):
    
    # on message
    async def on_process_message(self, message: types.Message, data: dict):
        session = UserSession(mycursor, message.chat.id).get_or_create()

        if not session.get("language"):
            reply_keyboard = language_keyboard()

            await message.answer(texts.choose_language_text, reply_markup=reply_keyboard)

            raise CancelHandler()

            

        
    # on callback
    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        session = UserSession(mycursor, call.from_user.id).get_or_create()

        call_type = json.loads(call.data)

        if not session.get("language") and isinstance(call_type, dict) and call_type.get("type") != 'choose_lang':
            reply_keyboard = language_keyboard()

            await bot.send_message(chat_id=call.from_user.id, text=texts.choose_language_text, reply_markup=reply_keyboard)

            raise CancelHandler()

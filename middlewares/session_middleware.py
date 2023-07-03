from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from cache import _cache
from user_session import UserSession


# session middleware
class SessionMiddleware(BaseMiddleware):
    async def on_pre_process_message(self, message: types.Message, data: dict):
        session = UserSession(_cache, message.chat.id)
        data['session'] = session
        data['session_data'] = session.get_or_create()

    async def on_pre_process_callback_query(self, call: types.CallbackQuery, data: dict):
        session = UserSession(_cache, call.from_user.id)
        data['session'] = session
        data['session_data'] = session.get_or_create()

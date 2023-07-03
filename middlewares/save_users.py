from aiogram.dispatcher.middlewares import BaseMiddleware
from db import User
from aiogram import types



# chack and change consultation status middleware
class SaveUsersMiddleware(BaseMiddleware):
    users = User()

    # save user to db on message
    async def on_process_message(self, message: types.Message, data: dict):
        if not self.users.single(message.chat.id):
            self.users.create(message.chat.id)

    # savve user to db on callback
    async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
        if not self.users.single(call.from_user.id):
            self.users.create(call.from_user.id)

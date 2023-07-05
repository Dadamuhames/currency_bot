from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from user_session import UserSession



# session middleware
class SessionMiddleware(BaseMiddleware):

    # def __init__(self):
    #     super().__init__()
    #     self.mydb = mysql.connector.connect(
    #         host=MYSQL_HOST,
    #         user=MYSQL_USER,
    #         password=MYSQL_PASSWORD,
    #         database=MYSQL_DB
    #     )

    #     self.mycursor = self.mydb.cursor()


    async def on_pre_process_message(self, message: types.Message, data: dict):
        session = UserSession(message.chat.id)
        data['session'] = session
        data['session_data'] = session.get_or_create()

    async def on_pre_process_callback_query(self, call: types.CallbackQuery, data: dict):
        session = UserSession(call.from_user.id)
        data['session'] = session
        data['session_data'] = session.get_or_create()

from aiogram.dispatcher.middlewares import BaseMiddleware
from db import MYSQL_DB, MYSQL_HOST, MYSQL_PASSWORD, MYSQL_USER
from aiogram import types
import mysql.connector

# chack and change consultation status middleware
class DataBaseMiddleWare(BaseMiddleware):
    # save user to db on message
    # async def on_process_message(self, message: types.Message, data: dict):
    #     mydb = mysql.connector.connect(
    #         host=MYSQL_HOST,
    #         user=MYSQL_USER,
    #         password=MYSQL_PASSWORD,
    #         database=MYSQL_DB
    #     )


    #     mycursor = mydb.cursor()

    #     data['mycursor'] = mycursor
    #     data['mydb'] = mydb


    # # savve user to db on callback
    # async def on_process_callback_query(self, call: types.CallbackQuery, data: dict):
    #     mydb = mysql.connector.connect(
    #         host=MYSQL_HOST,
    #         user=MYSQL_USER,
    #         password=MYSQL_PASSWORD,
    #         database=MYSQL_DB
    #     )


    #     mycursor = mydb.cursor()

    #     data['mycursor'] = mycursor
    #     data['mydb'] = mydb
    pass


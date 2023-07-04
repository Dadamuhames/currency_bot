from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
import json
from loader import *
from user_session import UserSession
from flags_dict import FLAGS as flags


# callback query filter
class QueryFilter(BoundFilter):
    key = 'query_filter'

    def __init__(self, c_type):
        self.c_type = c_type

    async def check(self, callback_query: types.CallbackQuery):
        callback_data = json.loads(callback_query.data)
        return callback_data.get('type') == self.c_type


dp.filters_factory.bind(QueryFilter, event_handlers=[dp.callback_query_handler])





async def currency_filter(message: types.Message):
    return message.text[:-2] in flags.keys()

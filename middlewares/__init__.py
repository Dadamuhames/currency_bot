from aiogram import Dispatcher
from .lang_required import *
from .save_users import *
from .session_middleware import *


def setup(dp: Dispatcher):
    dp.middleware.setup(LanguageRequired())
    dp.middleware.setup(SaveUsersMiddleware())
    dp.middleware.setup(SessionMiddleware())

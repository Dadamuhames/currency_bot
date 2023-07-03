from message_handlers import *
from callbacks import *
from loader import dp
from db import create_all_tables
from commands import *

if __name__ == '__main__':
    import middlewares

    create_all_tables()
    middlewares.setup(dp)
    executor.start_polling(dp, skip_updates=True)

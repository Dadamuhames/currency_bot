from message_handlers import *
from callbacks import *
from loader import dp
from db import *
from commands import *
from send_updates import broadcast_saveds
import asyncio
import aioschedule


async def scheduler():
    aioschedule.every().day.at("14:00").do(broadcast_saveds)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    import middlewares

    mydb = mysql.connector.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DB
    )

    mycursor = mydb.cursor()

    create_all_tables(mycursor)
    middlewares.setup(dp)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

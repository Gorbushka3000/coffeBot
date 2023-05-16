import os.path
from telegram.models.vsegdaCoffeDb import DATABASE_NAME
from aiogram.utils import executor
from telegram.view.alwaysCoffeBot import dp
from telegram.models.vsegdaCoffeDb import create_db


if __name__ == "__main__":
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        create_db()
    executor.start_polling(dp, skip_updates=True)



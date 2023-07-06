from aiogram import types


# admin main keyboard
def admin_main_keyboard():
    keyboard = types.ReplyKeyboardMarkup()

    first_row = [
        types.KeyboardButton(text="Статистика📊"),
        types.KeyboardButton(type="Рассылка🔈")
    ]

    keyboard.row(*first_row)

    return keyboard
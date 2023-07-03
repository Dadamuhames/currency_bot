from aiogram import types
import json
from flags_dict import FLAGS as flags


# main simple keyboard
def currencies_simple_keyboard():
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    default_currencies = ['USD', 'EUR', "RUB"]

    first_row = []

    for item in default_currencies:
        flag = flags.get(item, '')

        text = f"{item}{flag}"

        first_row.append(
            types.KeyboardButton(text=text)
        )

    reply_keyboard.row(*first_row)

    second_row = [
        types.KeyboardButton(text='Все валюты🌐'),
        types.KeyboardButton(text='Избранные💾'),
    ]

    reply_keyboard.row(*second_row)

    return reply_keyboard


# all currencies
def currencies_keyboard(currensies):
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    for i in range(0, len(currensies), 2):
        row = []

        code = currensies[i]['Ccy']
        flag = flags.get(code, '')
        text = f"{code}{flag}"

        row.append(
            types.KeyboardButton(text=text)
        )

        try:
            code = currensies[i+1]['Ccy']
            flag = flags.get(code, '')
            text = f"{code}{flag}"

            row.append(
                types.KeyboardButton(text=text)
            )
        except:
            pass


        reply_keyboard.row(*row)
    
    last_row = [types.KeyboardButton(text='Избранные💾')]

    reply_keyboard.row(*last_row)


    return reply_keyboard



# simple keyboard
def simple_keyboard():
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    rows = [
            types.KeyboardButton(text='Все валюты🌐'),
            # types.KeyboardButton(text='Назад🔙'),
        ] 

    reply_keyboard.row(*rows) 
        
    return reply_keyboard


# all and saved
def all_and_saved_keyboard():
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

    row = [
        types.KeyboardButton(text='Все валюты🌐'),
        types.KeyboardButton(text='Избранные💾'),
    ]

    reply_keyboard.row(*row) 

    return reply_keyboard





# save currency keyboard
def save_keyboard(saved, cur):
    reply_keyboard = types.InlineKeyboardMarkup()

    callback_dict = {
        "type": "save_currency",
        "currency": cur
    }


    if saved:
        text = "❤️"
    else:
        text = "🤍"


    reply_keyboard.add(
        types.InlineKeyboardButton(text=text, callback_data=json.dumps(callback_dict))
    )

    return reply_keyboard



# language keyboard
def language_keyboard():
    reply_keyboard = types.InlineKeyboardMarkup()

    ru = {
        "type": "choose_lang",
        "lang": "ru"
    }

    uz = {
        "type": "choose_lang",
        "lang": "uz"
    }

    row = [
        types.InlineKeyboardButton(
            text="Русский🇷🇺", callback_data=json.dumps(ru)),
        types.InlineKeyboardButton(
            text="O'zbek🇺🇿", callback_data=json.dumps(uz))
    ]

    reply_keyboard.row(*row)

    return reply_keyboard
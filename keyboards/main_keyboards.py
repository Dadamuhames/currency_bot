from aiogram import types
import json
from flags_dict import FLAGS as flags
import texts

# main simple keyboard
def currencies_simple_keyboard(lang):
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    default_currencies = ['USD', 'EUR', "RUB"]

    saved_text = texts.saved_btn.get(lang)
    all_text = texts.all_currs.get(lang)

    first_row = []

    for item in default_currencies:
        flag = flags.get(item, '')

        text = f"{item}{flag}"

        first_row.append(
            types.KeyboardButton(text=text)
        )

    reply_keyboard.row(*first_row)

    second_row = [
        types.KeyboardButton(text=all_text),
        types.KeyboardButton(text=saved_text),
    ]

    reply_keyboard.row(*second_row)

    return reply_keyboard


# all currencies
def currencies_keyboard(currensies, lang):
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    saved_text = texts.saved_btn.get(lang)
    menu_text = texts.menu_text.get(lang)

    first_row = [types.KeyboardButton(
        text=saved_text), types.KeyboardButton(text=menu_text)]

    reply_keyboard.row(*first_row)

    for i in range(0, len(currensies), 2):
        row = []

        code = currensies[i]['Ccy']

        if code == 'XDR':
            continue

        flag = flags.get(code, '')
        text = f"{code}{flag}"

        row.append(
            types.KeyboardButton(text=text)
        )

        try:
            code = currensies[i+1]['Ccy']

            if code == 'XDR':
                continue

            flag = flags.get(code, '')
            text = f"{code}{flag}"

            row.append(
                types.KeyboardButton(text=text)
            )
        except:
            pass


        reply_keyboard.row(*row)

    return reply_keyboard



# simple keyboard
def simple_keyboard(lang):
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    text = texts.all_currs.get(lang)

    rows = [
            types.KeyboardButton(text=text),
            # types.KeyboardButton(text='Назад🔙'),
        ] 

    reply_keyboard.row(*rows) 
        
    return reply_keyboard


# all and saved
def all_and_saved_keyboard(lang):
    reply_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    saved_text = texts.saved_btn.get(lang)
    all_text = texts.all_currs.get(lang)

    row = [
        types.KeyboardButton(text=all_text),
        types.KeyboardButton(text=saved_text),
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
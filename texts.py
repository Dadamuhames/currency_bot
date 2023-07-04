from flags_dict import FLAGS as flags

# currency text
def currency_text(lang, currency :dict): 
    code = currency.get("Ccy")

    if lang == "ru":
        text = f"""
            **Валюта**: {currency.get("CcyNm_RU")} {flags.get(code)} \n**Буквенный код**: {code} \n**Курс**: {currency.get("Rate")} сум \n**Разница**: {currency.get("Diff")} сум 
        """

    elif lang == "uz":
        text = f"""
            **Valyuta**: {currency.get("CcyNm_UZ")} {flags.get(code)} \n**Harf kodi**: {code} \n**Kursi**: {currency.get("Rate")} sum \n**Farq**: {currency.get("Diff")} sum
        """

    return text



choose_language_text = """ 
        🇷🇺 Выберите язык \n🇺🇿 Tilni tanlang     
     """


start_text = {
    "ru": """  Выберите валюту и узнайте текущий курс в Узбекских соммах. Сохраняйте интересующие вас валюты и получайте ежедневные обновления! """,
    "uz": """ Valyutani tanlang va o'zbek so'midagi joriy kursni bilib oling. Sizni qiziqtirgan valyutalarni saqlang va kundalik yangilanishlarni oling! """
}



there_is_no_saved = {
    "ru": "У вас еще нет сохраненных валют",
    "uz": "Sizda hali saqlagan valyutalar yo'q"
}


choose_curr = {
    "ru": "Выберите валюту",
    "uz": "Valyutani tanlang"
}


there_is_no_info = {
    "ru": "Об этой валюте пока еще информации нет",
    "uz": "Ushbu valyuta haqida hech qanday ma'lumot yo'q"
} 


error_text = {
    "ru": "Ошибка! Попробуйте еще раз!",
    "uz": "Xatolik yuz berdi! Yana bir bor urinib ko `ring!"
}

language_updated = {
    "ru": "Язык изменен на Русский🇷🇺",
    "uz": "Til O'zbek tiliga o'zgartirildi🇺🇿"
}


all_currs = {
    "ru": "Все валюты🌐",
    "uz": "Barcha valyutalar🌐"
}


saved_btn = {
    "ru": "Избранные💾",
    "uz": "Saqlangan💾"
}


updates_off = {
    "ru": "Уведомления об обновлениях отключены🔇\nУведомления можно снова включить командой /updatesOn",
    "uz": "Yangilash bildirishnomalari oʻchirilgan🔇 \nBildirishnomalarni /updatesOn buyrug'i bilan qayta yoqish mumkin"
}


updates_on = {
    "ru": "Уведомления об обновлениях включены🔈\nУведомления можно отключить командой /updatesOff",
    "uz": "Yangilash bildirishnomalari yoqilgan🔈\nBildirishnomalarni /updatesOff off buyrug'i bilan o'chirib qo'yish mumkin"
}


there_is_updates = {
    "ru": """Обновления по сохраненным вами валютам! 📢 \nОбновления будут приходить каждый день в 14:00! 🕒 \nОт обновлений можно отказатьсы комадой /updatesOff""",
    "uz": """Siz saqlagan valyutalar boʻyicha yangilanishlar! 📢 \nYangilanishlar har kuni soat 14:00 da keladi! 🕒 \nYangilanishlarni /updatesOff buyrugʻi bilan bekor qilish mumkin."""
}
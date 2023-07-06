import json
from db import User



class UserSession:
    def __init__(self, user_id):
        self.user_id = user_id
        self.user_model = User()

    # get session or create if there is no session yet
    def get_or_create(self):
        curent_session = {
            "language": None,
            "currencies": []
        }
        try:
            curent_user = self.user_model.single(self.user_id)
            
            if not curent_user:
                curent_user = self.user_model.create(self.user_id)

            curent_session['language'] = curent_user[2]
            curent_session['currencies'] = json.loads(curent_user[3]) if curent_user[3] else []
        except Exception as e:
            print("ERROR!", e)
            raise e

        return curent_session
    
    # add currency to session
    def add_currency(self, currency):
        try:
            curent_session = self.get_or_create()
            
            currencies_list = curent_session.get("currencies", [])
            
            if currency not in currencies_list:
                currencies_list.append(currency)

            self.user_model.update_currencies(self.user_id, json.dumps(currencies_list))

        except Exception as e:
            print('ERROR!', e)
            raise e

        return curent_session


    # delete currency
    def delete_currency(self, currency):
        try:
            curent_session = self.get_or_create()

            currencies_list = curent_session.get("currencies", [])

            if currency in currencies_list:
                currencies_list.remove(currency)

            self.user_model.update_currencies(self.user_id, json.dumps(currencies_list))

        except Exception as e:
            print("ERROR!", e)
            raise e

        return curent_session
    

    # add or delete
    def add_or_delete(self, currency):
        curent_session = self.get_or_create()

        currencies_list = curent_session.get("currencies", [])

        if currency in currencies_list:
            self.delete_currency(currency)
            return False
        
        else:
            self.add_currency(currency)
            return True



    # get currencies
    def get_currencies(self):

        # get curent session currencies
        current_session = self.get_or_create()

        currencies = current_session.get("currencies", [])

        return currencies if currencies else []


    # set language
    def set_language(self, lang):
        try:
            self.user_model.update_lang(self.user_id, lang)

            return True
        except Exception as e:
            print("ERROR!", e)

        return False

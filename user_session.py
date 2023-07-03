import json


class UserSession:
    def __init__(self, _cache, user_id):
        self._cache = _cache
        self.user_id = user_id

    # get session or create if there is no session yet
    def get_or_create(self):
        curent_session = self._cache.get(self.user_id)
        
        if not curent_session:
            curent_session = {
                "language": None,
                "currencies": [],
            }
            self._cache.set(self.user_id, json.dumps(curent_session))
        else:
            curent_session = json.loads(curent_session)

        return curent_session
    
    # add currency to session
    def add_currency(self, currency):
        curent_session = self.get_or_create()
        
        currencies_list = curent_session.get("currencies", [])
        
        if currency not in currencies_list:
            currencies_list.append(currency)

        curent_session["currencies"] = currencies_list
        self._cache.set(self.user_id, json.dumps(curent_session))

        return curent_session


    # delete currency
    def delete_currency(self, currency):
        curent_session = self.get_or_create()

        currencies_list = curent_session.get("currencies", [])

        if currency in currencies_list:
            currencies_list.remove(currency)

        curent_session["currencies"] = currencies_list
        self._cache.set(self.user_id, json.dumps(curent_session))

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
        curent_session = self.get_or_create()

        curent_session['language'] = lang

        self._cache.set(self.user_id, json.dumps(curent_session))

        return curent_session

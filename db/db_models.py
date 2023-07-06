from .db_config import *


# base model
class BaseChatModel:
    table = "" # database table name

    # list items
    def list(self):
        sql = f"SELECT * FROM {self.table}"
        db.execute(sql)
        queryset = db.cursor.fetchall()

        return queryset
    

    # single item
    def single(self, chat_id):
        sql = f"""SELECT * FROM users WHERE chat_id={chat_id}"""
        
        db.execute(sql)

        result = db.cursor.fetchone()

        return result


    # create item
    def create(self, chat_id):
        sql = f"INSERT INTO {self.table} (chat_id) VALUES (%s)"
        val = (chat_id, )
        db.execute(sql, val)
        db.connection.commit()



    # delete item
    def delete_user(self, chat_id):
        sql = f"DELETE FROM {self.table} WHERE chat_id = {chat_id}"
        db.execute(sql)

        db.connection.commit()




# user model
class User(BaseChatModel):
    table = 'users'

    # update item
    def update_lang(self, chat_id, lang):
        sql = f"""UPDATE {self.table} SET language = %s WHERE chat_id = %s"""
        db.execute(sql, (lang, chat_id))
        db.connection.commit()



    # update currencies
    def update_currencies(self, chat_id, currencies):
        sql = f"""UPDATE {self.table} SET currencies = %s WHERE chat_id = %s"""
        db.execute(sql, (currencies, chat_id))

        db.connection.commit()


    
    # change updates
    def change_updates(self, chat_id, updates):
        sql = f"""UPDATE {self.table} SET updates = %s WHERE chat_id = %s"""
        db.execute(sql, (updates, chat_id))

        db.connection.commit()



    # get updates active
    def get_updatable_users(self):
        sql = f"SELECT chat_id FROM {self.table} WHERE updates = 1"
        db.execute(sql)
        queryset = db.cursor.fetchall()

        return queryset



# group model
class Group(BaseChatModel):
    table = 'groups'
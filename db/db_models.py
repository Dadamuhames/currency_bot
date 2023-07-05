from .db_config import *


# base model
class BaseChatModel:
    table = "" # database table name

    # list items
    def list(self):
        sql = f"SELECT * FROM {self.table}"
        mycursor.execute(sql)
        queryset = mycursor.fetchall()

        return queryset
    

    # single item
    def single(self, chat_id):
        sql = f"""SELECT * FROM users WHERE chat_id={chat_id}"""
        
        mycursor.execute(sql)

        result = mycursor.fetchone()

        return result


    # create item
    def create(self, chat_id):
        sql = f"INSERT INTO {self.table} (chat_id) VALUES (%s)"
        val = (chat_id, )
        mycursor.execute(sql, val)
        mydb.commit()



    # delete item
    def delete_user(self, chat_id):
        sql = f"DELETE FROM {self.table} WHERE chat_id = {chat_id}"
        mycursor.execute(sql)

        mydb.commit()




# user model
class User(BaseChatModel):
    table = 'users'

    # update item
    def update_lang(self, chat_id, lang):
        sql = f"""UPDATE {self.table} SET language = %s WHERE chat_id = %s"""
        mycursor.execute(sql, (lang, chat_id))
        mydb.commit()



    # update currencies
    def update_currencies(self, chat_id, currencies):
        sql = f"""UPDATE {self.table} SET currencies = %s WHERE chat_id = %s"""
        mycursor.execute(sql, (currencies, chat_id))

        mydb.commit()


    
    # change updates
    def change_updates(self, chat_id, updates):
        sql = f"""UPDATE {self.table} SET updates = %s WHERE chat_id = %s"""
        mycursor.execute(sql, (updates, chat_id))

        mydb.commit()



    # get updates active
    def get_updatable_users(self):
        sql = f"SELECT chat_id FROM {self.table} WHERE updates = 1"
        mycursor.execute(sql)
        queryset = mycursor.fetchall()

        return queryset



# group model
class Group(BaseChatModel):
    table = 'groups'
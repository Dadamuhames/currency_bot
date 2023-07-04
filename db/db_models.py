from .db_config import *


# base model
class BaseChatModel:
    table = "" # database table name

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )


        self.mycursor = self.mydb.cursor()

    # list items
    def list(self):
        sql = f"SELECT * FROM {self.table}"
        self.mycursor.execute(sql)
        queryset = self.mycursor.fetchall()

        self.mycursor.close()
        return queryset
    

    # single item
    def single(self, chat_id):
        sql = f"""SELECT * FROM users WHERE chat_id={chat_id}"""
        
        self.mycursor.execute(sql)

        result = self.mycursor.fetchone()

        self.mycursor.close()
        return result


    # create item
    def create(self, chat_id):
        sql = f"INSERT INTO {self.table} (chat_id) VALUES (%s)"
        val = (chat_id, )
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        self.mycursor.close()



    # delete item
    def delete_user(self, chat_id):
        sql = f"DELETE FROM {self.table} WHERE chat_id = {chat_id}"
        self.mycursor.execute(sql)

        self.mydb.commit()
        self.mycursor.close()




# user model
class User(BaseChatModel):
    table = 'users'

    # update item
    def update_lang(self, chat_id, lang):
        sql = f"""UPDATE {self.table} SET language = %s WHERE chat_id = %s"""
        self.mycursor.execute(sql, (lang, chat_id))

        self.mydb.commit()
        self.mycursor.close()



    # update currencies
    def update_currencies(self, chat_id, currencies):
        sql = f"""UPDATE {self.table} SET currencies = %s WHERE chat_id = %s"""
        self.mycursor.execute(sql, (currencies, chat_id))

        self.mydb.commit()
        self.mycursor.close()


    
    # change updates
    def change_updates(self, chat_id, updates):
        sql = f"""UPDATE {self.table} SET updates = %s WHERE chat_id = %s"""
        self.mycursor.execute(sql, (updates, chat_id))

        self.mydb.commit()
        self.mycursor.close()



    # get updates active
    def get_updatable_users(self):
        sql = f"SELECT chat_id FROM {self.table} WHERE updates = 1"
        self.mycursor.execute(sql)
        queryset = self.mycursor.fetchall()
        self.mycursor.close()

        return queryset



# group model
class Group(BaseChatModel):
    table = 'groups'
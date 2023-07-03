from .db_config import mycursor, mydb


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


# group model
class Group(BaseChatModel):
    table = 'groups'
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()


MYSQL_USER = os.environ.get("MYSQL_USER")
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD')
MYSQL_DB = os.environ.get("MYSQL_DB")
MYSQL_HOST = os.environ.get("MYSQL_HOST")




class DataBase:
    def __init__(self):
        self.connection = self.create_connection()
        self.cursor = self.connection.cursor()

    def create_connection(self):
        mydb = mysql.connector.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB
        )

        return mydb
    
    
    def execute(self, query, values=None):
        try:
            cursor = self.cursor

            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
        
        except mysql.connector.errors.DatabaseError:
            self.connection.close()
            self.connection = self.create_connection()
            self.cursor = self.connection.cursor()
            return self.execute(query, values=values)


db = DataBase()
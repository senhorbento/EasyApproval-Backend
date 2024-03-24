import sqlite3
from .Constants import connection_string

class DB:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = sqlite3.connect(connection_string)
            self.cursor = self.conn.cursor()
        except sqlite3.Error as e:
            print("Error connecting to SQLite database:", e)

    def disconnect(self):
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute(self, query, parameters=None, fetch=False):
        try:
            if not self.conn:
                self.connect()
            if parameters:
                self.cursor.execute(query, parameters)
            else:
                self.cursor.execute(query)
            if fetch:
                return self.cursor.fetchall()
            else:
                self.conn.commit()
        except sqlite3.Error as e:
            print("Error executing query:", e)
        finally:
            if not fetch:
                self.disconnect()

    def create_table(self, create_table_query):
        self.execute(create_table_query)

    def execute_return(self, query, parameters=None):
        return self.execute(query, parameters, fetch=True)

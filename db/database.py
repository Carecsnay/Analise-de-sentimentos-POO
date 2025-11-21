import sqlite3

class Database:
    def __init__(self,db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS analysis (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            post TEXT NOT NULL,
            category TEXT,
            active BOOLEAN
            )
        """)
        self.connect.commit()
    
    def insert_post(self, post, category):
        self.cursor.execute("INSERT INTO analysis (post, category) VALUES (?,?)", (post, category))
        self.connect.commit()

    def read_posts(self):
        self.cursor.execute("SELECT * FROM analysis")
        return self.cursor.fetchall()
    
    def __del__(self):
        self.connect.close()

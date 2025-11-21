import sqlite3

from .models import Post

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
            active BOOLEAN,
            score FLOAT
            )
        """)
        self.connect.commit()
        print('DB criado com sucesso!')
    
    def insert_post(self, post, category, active=True, score=None):
        self.cursor.execute("INSERT INTO analysis (post, category, active, score) VALUES (?,?,?,?)", (post, category, active, score))
        self.connect.commit()

    def read_posts(self):
        self.cursor.execute("SELECT * FROM analysis")
        rows = self.cursor.fetchall()
        posts = []
        for row in rows:
            posts.append(Post(id=row[0], post=row[1], category=row[2], active=bool(row[3]), score=row[4]))
        return posts
    
    def update_post(self, post_id, post, category, active, score):
        self.cursor.execute("UPDATE analysis SET post = ?, category = ?, active = ?, score = ? WHERE id = ?",
                            (post, category, active, score, post_id))
        self.connect.commit()

    def __del__(self):
        self.connect.close()
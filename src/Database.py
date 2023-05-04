import sqlite3
import os
class Database:
    def __init__(self, db):
        self.db = db
        self.conn = sqlite3.connect(self.db)
        self.conn.row_factory = self.dict_factory
        self.c = self.conn.cursor()
        self.c.execute('CREATE TABLE IF NOT EXISTS file (id INTEGER PRIMARY KEY AUTOINCREMENT, original_file TEXT, hashable_file TEXT)')
        self.conn.commit()

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d
    
    def insert(self, original_file, hashable_file):
        self.c.execute('INSERT INTO file (original_file, hashable_file) VALUES (?, ?)', (original_file, hashable_file))
        self.conn.commit()
        return self.c.lastrowid
    
    def get(self, id):
        self.c.execute('SELECT * FROM file WHERE id=?', (id,))
        return self.c.fetchone()
    
    def get_all(self):
        self.c.execute('SELECT * FROM file')
        return self.c.fetchall()
    
    def delete(self, id):
        self.c.execute('SELECT * FROM file WHERE id=?', (id,))
        # Get the Assoc data 
        data = self.c.fetchone()
        if data == None:
            return False
        # Delete the file
        self.c.execute('DELETE FROM file WHERE id=?', (id,))
        self.conn.commit()
        # Delete the file
        DIRNAME = os.path.dirname(__file__)
        print(data)
        os.remove(DIRNAME + '/../resources/' + data['hashable_file'])
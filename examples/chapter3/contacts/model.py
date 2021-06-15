import sqlite3

class ContactBook:
    def __init__(self, dbFile=None):
        if dbFile:
            self.db = sqlite3.connect(dbFile)
            self.cur = self.db.cursor()
        else:
            self.db = None
            self.cur = None

    def loadBook(self, dbFile):
        # Check if a contact book is not already loaded
        if self.db:
            self.cur.close()
            self.db.close()

        self.db = sqlite3.connect(dbFile)
        self.cur = self.db.cursor()

     def createBook(self, dbFile):
        if self.db:
            return
        self.db = sqlite3.connect(dbFile)
        self.cur = self.db.cursor()
        stmt = """CREATE TABLE contacts(
                  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                  name TEXT NOT NULL,
                  phone TEXT NOT NULL,
                  address TEXT,
                  email TEXT);"""
        self.cur.execute(stmt)
        self.db.commit()
   
    def addContact(self, name, phone, addr=None, email=None):
        stmt = """INSERT INTO contacts
                  (name, phone, address, email)
                  VALUES (?, ?, ?, ?)"""
        self.cur.execute(stmt, (name, phone, addr, email))
        self.db.commit()

    def stop(self):
        self.db.close()

    def __del__(self):
        self.db.close()

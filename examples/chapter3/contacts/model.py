import sqlite3
import re

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

        if not self.isInited():
            self.createBook()
        self.db.create_function("REGEXP", 2, regexp)

    def createBook(self):
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

    def deleteContact(self, np):
        stmt = """DELETE FROM contacts
                  WHERE
                  name REGEXP ? OR
                  phone REGEXP ?"""
        res = self.cur.execute(stmt, (np, np))
        self.db.commit()
        return res.rowcount > 0

    def getAllContacts(self):
        stmt = "SELECT name, phone, address, email FROM contacts"
        self.cur.execute(stmt)
        return self.cur.fetchall()

    def searchByParam(self, param, value):
        """ Search for a contact by phone number """
        stmt = """SELECT name, phone, address, email
                FROM
                contacts
                WHERE
                {} REGEXP ?""".format(param)
        self.cur.execute(stmt, [value])
        return self.cur.fetchall()

    def isInited(self):
        """ Determine if database has been setup as a contact book yet """
        stmt = "SELECT name FROM sqlite_master WHERE type='table' AND name='contacts'"
        self.cur.execute(stmt)
        res = self.cur.fetchall()
        return len(res) == 1

    def stop(self):
        if self.db:
            self.cur.close()
            self.db.close()

    def __del__(self):
        self.stop()

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

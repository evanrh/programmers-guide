import sqlite3

class DBConnector:
    """ A wrapper to create and manage a database of users and entry times """
    def __init__(self, dbFile=""):
        if dbFile:
            self.con = sqlite3.connect(dbFile)
            self.cursor = self.con.cursor()
        else:
            self.con = None
            self.cursor = None

    def createDB(self, fname='visits.db'):
        self.con = sqlite3.connect(dbFile)
        self.cursor = self.con.cursor()

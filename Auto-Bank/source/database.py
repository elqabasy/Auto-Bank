import sqlite3
# from constants import *


import sqlite3, shutil, os, datetime


class Database:
    def __init__(self, DBName:str="database.db") -> None:
        self.DBCursor = None
        self.DBFile = str(DBName).strip()
        self.DBSql = sqlite3.connect(self.DBFile)
        self.DBCursor = self.DBSql.cursor()

    def Execute(self,Query:str=None, params:dict=None):
        if self.DBCursor and Query:
            try:
                if params:
                    self.DBCursor.execute(Query, params)
                else:
                    self.DBCursor.execute(Query)

                Data = self.DBCursor.fetchall()
                self.DBSql.commit()
                return Data
            except Exception as Error:
                return Error
        return False

    def Query(self,Query:str=None, params:dict=None):
        if Query:
            if params:
                self.DBCursor.execute(Query, params)
            else:
                self.DBCursor.execute(Query)

            Result = self.DBCursor.fetchall()
            return Result

    def Close(self):
        try:
            self.DBSql.close()
        except Exception as Error:
            return Error


DATABASE = Database()


# banks
Result = DATABASE.Query("""
CREATE TABLE IF NOT EXISTS `Banks`(
    `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name` TEXT NOT NULL UNIQUE,
    `Serial` VARCHAR(11) NOT NULL UNIQUE

);""")

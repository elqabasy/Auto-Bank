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
    
    # def Backup(self, name:str=None):
    #     if name:
    #         path = os.path.abspath(name)
    #     else:
    #         path = os.path.join(BACKUP_DIR,"Backup_{currentDate}_.db".format(currentDate=datetime.datetime.today().strftime("%d-%m-%Y")))

    #     return shutil.copy(self.DBFile, path)



DATABASE = Database()

# Create Tables
# banks
Result = DATABASE.Query("""
CREATE TABLE IF NOT EXISTS `Banks`(
    `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name` TEXT NOT NULL UNIQUE,
    `Serial` VARCHAR(11) NOT NULL UNIQUE

);""")
# print(Result)

# creators
Result = DATABASE.Query("""
CREATE TABLE IF NOT EXISTS `Creators`(
    `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name` TEXT NOT NULL UNIQUE
);""")
# print(Result)

# accounts
Result = DATABASE.Query("""
CREATE TABLE IF NOT EXISTS `Accounts`(
    `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Number` TEXT NOT NULL UNIQUE,
    `CreatorID` INT NOT NULL,
    FOREIGN KEY (`CreatorID`) REFERENCES `Creators` (`ID`) 
);""")
# print(Result)

# Types
Result = DATABASE.Query("""
CREATE TABLE IF NOT EXISTS `Types`(
    `ID` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `Name` TEXT NOT NULL UNIQUE
);
""")
# print(Result)
if __name__ == "__main__":
    try:
        DATABASE = Database()
    except Exception as Error:
        print(Error)
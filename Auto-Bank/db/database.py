# builtin packages
import sqlite3

# me


class Database:
    def __init__(self, DBName: str) -> None:
        self.DBCursor = None
        self.DBFile = str(DBName).strip()
        self.DBSql = sqlite3.connect(self.DBFile)
        self.DBCursor = self.DBSql.cursor()

    def Execute(self, Query: str = None, params: dict = None):
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

    def Query(self, Query: str = None, params: dict = None):
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


class BankDatabase(Database):
    def __init__(self, DBName: str) -> None:
        super().__init__(DBName)

    def getData(self):
        QUERY_STR: str = "SELECT Name, Serial FROM `Banks`;"
        RESULT: str = self.Query(QUERY_STR)
        return RESULT

    def getBankName(self, code: str):
        pass

    def getBankCode(self, name: str):
        name = str(name).strip()
        QUERY_STR: str = "SELECT Serial FROM `Banks` WHERE Name = ?"
        RESULT: str = self.Query(QUERY_STR, (name,))
        return RESULT

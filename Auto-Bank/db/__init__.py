# package
from .database import BankDatabase
from settings import SC, Settings

# DATABASE
DATABASE = BankDatabase(SC.get(Settings.Database.Path.value, "database.db"))
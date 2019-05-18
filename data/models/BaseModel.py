from peewee import *

db = SqliteDatabase('data/bot.db')

class BaseModel(Model):
    class Meta:
        database = db
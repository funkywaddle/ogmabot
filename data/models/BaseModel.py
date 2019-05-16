from peewee import *

db = SqliteDatabase('data/bot.db')

class GKGModel(Model):
    class Meta:
        database = db
from peewee import *
from data.models.BaseModel import BaseModel

class Quotes(BaseModel):
    quote = TextField()

    @classmethod
    def select_random(cls):
        return cls.select().order_by(fn.Random()).limit(1).get()
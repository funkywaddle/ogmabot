from peewee import *
from data.models.BaseModel import BaseModel

class Suggestion(BaseModel):
    suggestion = TextField()
    user = TextField()

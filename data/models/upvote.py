from peewee import *
from data.models.BaseModel import BaseModel
from data.models.suggestion import Suggestion

class Upvote(BaseModel):
	suggestion = ForeignKeyField(Suggestion, backref='upvotes')
	user = TextField()

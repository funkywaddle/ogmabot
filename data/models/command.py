from peewee import *
from data.models.BaseModel import BaseModel

class Command(BaseModel):
	command = CharField()
	response = TextField()

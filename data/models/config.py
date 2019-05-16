from peewee import *
from data.models.BaseModel import BaseModel

class Config(BaseModel):
	key = CharField()
	value = CharField()

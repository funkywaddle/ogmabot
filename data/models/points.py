from peewee import *
from data.models.BaseModel import BaseModel

class Points(BaseModel):
	user = CharField()
	points = IntegerField()

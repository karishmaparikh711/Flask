import flask
from application import db
from werkzeug.security import generate_password_hash, check_password_hash

class Admin(db.Document):
	username =db.StringField( max_length=50,unique=True )
	password = db.StringField( max_length=50,unique=True )
	def set_password(self, password):
		self.password = password

	def get_password(self, password):
		return self.password

		
class Patient(db.Document):
	ssnid = db.IntField( max_length=50,unique=True)
	name  =  db.StringField(max_length=50)
	age =  db.IntField(max_length=50)
	address = db.StringField(max_length=50)
	dateofadmit = db.StringField(max_length=50)
	typeofbed = db.StringField(max_length=50)
	city = db.StringField(max_length=50)
	state = db.StringField(max_length=50)


	  
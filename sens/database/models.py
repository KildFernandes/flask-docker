from sens.__init__ import db

class Usuario(db.Document):
    name = db.StringField(required=True)
    email = db.StringField(required=True, unique=True)
    msg = db.ListField(required=False)
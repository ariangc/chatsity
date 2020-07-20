from app import db
from models.utils import AddUpdateDelete

class Chatroom(AddUpdateDelete, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(256))
    messages = db.relationship("Message")

    def to_json(self):
        return {
            'id_chatroom' : self.id,
            'name': self.name,
            'description': self.description
        }

from app import db
from models.utils import AddUpdateDelete

class Message(AddUpdateDelete, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1000))
    timestamp = db.Column(db.DateTime)
    
    id_user = db.Column('id_user', db.ForeignKey('user.id'))
    id_chatroom = db.Column('id_chatroom', db.ForeignKey('chatroom.id'))

    def to_json(self):
        return {
            'id_message': self.id,
            'body': self.body,
            'timestamp': self.timestamp,
            'id_user': self.id_user,
            'id_chatroom': self.id_chatroom
        }
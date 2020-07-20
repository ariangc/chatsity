from models.user import User
from models.message import Message
from models.chatroom import Chatroom
from flask import request
from resources.security import AuthRequiredResource
import status
import datetime
from app import db

class MessageListResource(AuthRequiredResource):
    def get(self):
        request_dict = request.get_json()
        if not request_dict:
            response = {"error": "No input data provided."}
            return response, status.HTTP_400_BAD_REQUEST
        
        id_chatroom = request_dict['id_chatroom']

        messages = Message.query.filter_by(id_chatroom=id_chatroom).order_by(Message.timestamp.desc()).limit(50)[::-1]

        response = {
            'messages': []
        }

        for message in messages:
            message_json = message.to_json()
            response['messages'].add(message_json)
        
        return response, status.HTTP_200_OK

    def post(self):
        request_dict = request.get_json()
        if not request_dict:
            response = {"error": "No input data provided."}
            return response, status.HTTP_400_BAD_REQUEST

        try:
            id_user = int(request_dict['id_user'])
            id_chatroom = int(request_dict['id_chatroom'])
            msg_body = request_dict['msg_body']
            if msg_body[0] == '/':
                raise NotImplementedError     

            message = Message(
                body=msg_body, 
                timestamp=datetime.datetime.utcnow(), 
                id_user=id_user, 
                id_chatroom=id_chatroom
            )
            message.add(message)
            db.session.commit()

            response = {"ok": "Message published successfully on room %d" % id_chatroom }
            return response, status.HTTP_200_OK
        except Exception as e:
            db.session.rollback()
            response = {"error": str(e)}
            return response, status.HTTP_400_BAD_REQUEST

class GetByChatroom(AuthRequiredResource):
    def get(self):
        id_chatroom = int(request.args.get('id_chatroom'))
        messages = Message.query.filter_by(id_chatroom=id_chatroom).order_by(Message.timestamp.desc()).limit(50)

        response = {
            'messages': []
        }

        for message in messages:
            sender = User.query.get_or_404(message.id_user)
            timestamp = message.timestamp.strftime("%H:%M")
            body = message.body

            message_dict = {
                'sender': sender.name,
                'timestamp': timestamp,
                'body': body
            }
            response['messages'].append(message_dict)
        
        return response, status.HTTP_200_OK
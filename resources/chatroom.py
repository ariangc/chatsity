from models.user import User
from models.message import Message
from models.chatroom import Chatroom
from flask import request
from resources.security import AuthRequiredResource
import status
import datetime
from flask_restful import Resource

class ChatroomResource(AuthRequiredResource):
    def get(self, id):
        try:
            chatroom = Account.query.get_or_404(id)
            response = chatroom.to_json()
            return response, status.HTTP_200_OK
        except Exception as e:
            response = {"error": str(e)}
            return response, status.HTTP_400_BAD_REQUEST

class ChatroomListResource(Resource):
    def get(self):
        try:
            chatrooms = Chatroom.query.all()
            response = {
                'chatrooms' : []
            }
            for chatroom in chatrooms:
                chatroom_dict = chatroom.to_json()
                response['chatrooms'].append(chatroom_dict)
            return response, status.HTTP_200_OK
        except Exception as e:
            response = {"error": str(e)}
            return response, status.HTTP_200_OK

    def put(self):
        try:
            request_dict = request.get_json()
            if not request_dict:
                response = {"error": "No input data provided."}
                return response, status.HTTP_400_BAD_REQUEST
            
            name = request_dict['name']
            description = (request_dict['description'] if 'description' in request_dict['description'] else "")

            chatroom = Chatroom(name=name, description=description)
            chatroom.add(chatroom)
            db.session.commit()

            response = {"ok": "Added chatroom successfully."}
            return response, status.HTTP_200_OK
        except Exception as e:
            response = {"error": str(e)}
            return response, status.HTTP_200_OK
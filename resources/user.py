from models.user import User
from models.message import Message
from models.chatroom import Chatroom
from flask import request
from resources.security import AuthRequiredResource
import status
import datetime

class UserResource(AuthRequiredResource):
    def get(self, id):
        try:
            user = User.query.get_or_404(id)
            response = user.to_json()

            return response, status.HTTP_200_OK
        except Exception as e:
            response = {"error": str(e)}
            return response, status.HTTP_400_BAD_REQUEST
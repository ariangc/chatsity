from models.user import User
from models.message import Message
from models.chatroom import Chatroom
from flask import request
from resources.security import AuthRequiredResource
import status
import datetime
from flask import make_response, render_template, g

class ChatGUIResource(AuthRequiredResource):
    def get(self):
        id_chatroom = int(request.args.get('id_chatroom'))
        user_details = {
            'email': g.user.email,
            'password': g.user.password,
            'name': g.user.name,
            'id_user': g.user.id
        }

        chatroom = Chatroom.query.get_or_404(id_chatroom)

        chatroom_details = {
            'name': chatroom.name,
            'description': chatroom.description,
            'id_chatroom': str(id_chatroom)
        }

        return make_response(render_template(
                                'chatroom.html', 
                                user=user_details, 
                                chatroom=chatroom_details
                            ))
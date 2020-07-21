#!/usr/bin/env python

"""
      views.py
      ----------
      This module register all resources/services that the app will
      contain into a blueprint, which is also registered into the
      app itself.
"""

__author__ = "Arian Gallardo"

from flask import Blueprint
from flask_restful import Api, Resource

from resources.authentication import SignupResource, LoginResource, LogoutResource, VerifyTokenResource
from resources.user import UserResource
from resources.chatroom import ChatroomResource, ChatroomListResource
from resources.message import MessageListResource, GetByChatroom
from resources.chat_gui import ChatGUIResource
from resources.signup_gui import SignupGUIResource

api_blueprint = Blueprint('api', __name__)
api = Api(api_blueprint)

api.add_resource(SignupResource, '/signup')
api.add_resource(LoginResource, '/login')
api.add_resource(LogoutResource, '/logout')
api.add_resource(VerifyTokenResource, '/verify')
api.add_resource(UserResource, '/user')
api.add_resource(ChatroomResource, '/chatroom/<int:id>')
api.add_resource(ChatroomListResource, '/chatroom')
api.add_resource(MessageListResource, '/message')
api.add_resource(GetByChatroom, '/bychatroom')
api.add_resource(ChatGUIResource, '/chat')
api.add_resource(SignupGUIResource, '/signup')
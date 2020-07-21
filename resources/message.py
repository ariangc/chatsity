#!/usr/bin/env python

"""
    message.py
    ----------
    This module implements the necessary functions to create and read
    message information.
"""

__author__ = "Arian Gallardo"

from models.user import User
from models.message import Message
from models.chatroom import Chatroom
from flask import request
from resources.security import AuthRequiredResource
import status
import datetime
from app import db
import pika

class MessageListResource(AuthRequiredResource):
    "Resource to manage all messages information."
    def get(self):
        """ GET request handler for MessageListResource. It retrieves
            all message information from a chatroom given a chatroom id.

            In case of an error, HTTP status 400 (BAD_REQUEST) is returned.
            Else, HTTP status 200 (OK) is returned.
        """
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
            response['messages'].append(message_json)
        
        return response, status.HTTP_200_OK

    def post(self):
        """ POST request handler for MessageListResource. It publishes a
            new message from a user to a specific chatroom given user id
            and chatroom id. 

            It handles bot invoking requests. When a message is sent with
            an slash character ('/') at the begginning, it calls the
            decoupled bot requesting the information that should be obtained
            from the command. Uses pika to produce this AMQP request.

            In case of an error, HTTP status 400 (BAD_REQUEST) is returned.
            Else, HTTP status 200 (OK) is returned.
        """
        request_dict = request.get_json()
        if not request_dict:
            response = {"error": "No input data provided."}
            return response, status.HTTP_400_BAD_REQUEST

        try:
            id_user = int(request_dict['id_user'])
            id_chatroom = int(request_dict['id_chatroom'])
            msg_body = request_dict['msg_body']
            if msg_body[0] == '/':
                bot_body = msg_body + "$" + str(id_user) + "#" + str(id_chatroom)

                connection = pika.BlockingConnection(
                    pika.ConnectionParameters(host='localhost')
                )
                channel = connection.channel()
                channel.queue_declare(queue='financial')
                channel.basic_publish(exchange='', routing_key='financial', body=bot_body)
                print(" [x] Sent " + bot_body)
                connection.close()

                response = {"ok": "Message sent to bot successfully"}
                return response, status.HTTP_200_OK

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
    "Resource to get messages given a chatroom."
    def get(self):
        """ GET request handler for GetByChatroom. It retrieves
            last 50 messages information from a chatroom given a chatroom id.
        """
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
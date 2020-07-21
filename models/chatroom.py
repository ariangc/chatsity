#!/usr/bin/env python

"""
    chatroom.py
    ----------
    This module contains the declaration of the Chatroom database model.
"""

__author__ = "Arian Gallardo"

from app import db
from models.utils import AddUpdateDelete

class Chatroom(AddUpdateDelete, db.Model):
    "Class Chatroom to provide data access to information of registered chatrooms."
    __tablename__ = 'chatroom'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(256))
    messages = db.relationship("Message")

    def to_json(self):
        "Returns a dictionary with chatroom information."
        return {
            'id_chatroom' : self.id,
            'name': self.name,
            'description': self.description
        }

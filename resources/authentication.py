#!/usr/bin/env python

"""
      authentication.py
      ----------
      Handles authentication resources for users, storing and retrieving their information
      from a database.
"""

__author__ = "Arian Gallardo"

from models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from resources.utils import password_policy
from flask import request, jsonify, make_response, g, render_template
from app import db
from resources.security import Verify_password
import status
from flask_restful import Resource
from sqlalchemy.exc import SQLAlchemyError

class SignupResource(Resource):
    " Resource to register a new user to the system. "
    def post(self):
        """ POST request handler for SignupResource. Creates a new
            user on the database by their data. The necessary information
            about the user is: email, password and name.

            Return user information and an Authentication Token if creation
            was successful. Returns an error otherwise.

            In case of an error, HTTP status 400 (BAD_REQUEST) is returned.
            Else, HTTP status 200 (OK) is returned.
        """
        request_dict = request.get_json()
        if not request_dict:
            response = {"error": "No input data provided."}
            return response, status.HTTP_400_BAD_REQUEST

        email = request_dict['email']
        password = request_dict['password']
        name = request_dict['name']

        user = User.query.filter_by(email=email).first()
        
        if user:
            response = {"error": "Email address already exists."}
            return response, status.HTTP_400_BAD_REQUEST
        print(password)
        if len(password_policy.test(password)):
            response = {"error": "Please check password strength. It should have at least 5 characters, 1 uppercase letter, 1 number and 1 special character."}
            print("passpolicy")
            return response, status.HTTP_400_BAD_REQUEST
               
        new_user = User(email=email, password=generate_password_hash(password, method='sha256'), name=name)

        try:
            db.session.add(new_user)
            db.session.commit()

            user = User.query.filter_by(email=email).first()
            token = user.GenerateAuthToken()
            user.token = token.decode('ascii')
            g.user = user
            user.update()
            db.session.commit()
            
            response = {
                'email': user.email,
                'id': user.id,
                'token': user.token
            }

            return response, status.HTTP_200_OK
        except SQLAlchemyError as e:
            db.session.rollback()
            response = {"error": str(e)}
            return response, status.HTTP_400_BAD_REQUEST

class LoginResource(Resource):
    " Resource to login a previously created user to the system. "
    def post(self):
        """ POST request handler for LoginResource. Checks for a registered
            user on the database for the corresponding credentials and retrieves
            information of it in case of success.

            Return user information and an Authentication Token if login
            was successful. Returns an error otherwise.

            In case of an error, HTTP status 400 (BAD_REQUEST) is returned.
            Else, HTTP status 200 (OK) is returned.
        """
        request_dict = request.get_json()
        if not request_dict:
            response = {"error": "No input data provided"}
            return response, status.HTTP_400_BAD_REQUEST
        
        response = {}

        try:
            email = request_dict['email']
            password = request_dict['password']

            user = User.query.filter_by(email=email).first()

            if not user or not check_password_hash(user.password, password):
                response = {'error': 'Please check your login credentials and try again.'}
                return response, status.HTTP_400_BAD_REQUEST

            
            token = user.GenerateAuthToken()
            user.token = token.decode('ascii')
            g.user = user
            user.update()
            db.session.commit()

            response = {
                'email': user.email,
                'id' : user.id,
                'name': user.name
            }

            token_dict = {'token' : user.token}
            response.update(token_dict)
            return response, status.HTTP_200_OK
        except Exception as e:
            db.session.rollback()
            response = {"error": str(e)}

        return response, status.HTTP_200_OK

class VerifyTokenResource(Resource):
    " Resource to verify HTTP token authenticity."
    def get(self):
        """ GET request handler for VerifyTokenResource. Verifies if the
            provided token is authentic and has not expired yet.

            In case of an error, HTTP status 400 (BAD_REQUEST) is returned.
            Else, HTTP status 200 (OK) is returned.
        """
        request_dict = request.get_json()
        if not request_dict:
            response = {'error': 'No input data provided'}
            return response, status.HTTP_400_BAD_REQUEST
        
        token = request_dict['token']
        valid = Verify_password(token, "unused")
        response = {
            'valid': valid
        }
        return response, status.HTTP_200_OK

class LogoutResource(Resource):
    " Resource to Logout from a session "
    def get(self):
        """ GET requesto handler for LogoutResource. This was intended
            to implement logout functionality. Declared for scalability
            reasons.
        """
        response = {
            'ok': 'Logged out succesfully.'
        }
        return make_response(render_template('logout.html'))

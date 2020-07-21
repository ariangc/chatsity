from flask import make_response, render_template
from flask_restful import Resource

class SignupGUIResource(Resource):
    def get(self):
        return make_response(render_template('signup.html'))
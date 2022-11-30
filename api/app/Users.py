from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

from app import app
from config import client

collection = client['users']

api = Api(app)

class Users(Resource):
    def get(self, name):
        return 'awen'
        

api.add_resource(Users, "/users/<string:name>")
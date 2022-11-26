from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

from app import app

from Users import Users
from Items import Items

api = Api(app)

api.add_resource(Users, "/user");
api.add_resource(Items, "/items");
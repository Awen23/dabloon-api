from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

from config import client 

db = client.dabloons
collection = db.users

user_put_args = reqparse.RequestParser();
user_put_args.add_argument("name", type=str, help="Username is required", required=True);
user_put_args.add_argument("user_details", type=str, help="Identifier is required", required=True);
user_put_args.add_argument("balance", type=int, help="Balance");

def abort_if_user_doesnt_exist(user_id):
    if collection.find_one({"identifier": user_id}) is None:
        abort(404, message="User doesn't exist")
        
def abort_if_user_exists(user_id):
    if collection.find_one({"identifier": user_id}) is not None:
        abort(409, message="User already exists")

@app.route('/user', methods=['POST'])
def put(self, user_id):
    abort_if_user_exists(user_id)
    args = user_put_args.parse_args()
    collection.insert_one({"identifier": user_id, "name": args["name"], "balance": args["balance"]})

@app.route('/user', methods=['PATCH'])
def patch(self, user_id):
    abort_if_user_doesnt_exist(user_id)
    args = user_put_args.parse_args()
    collection.update_one({"identifier": user_id}, {"$set": {"balance": args["balance"]}})

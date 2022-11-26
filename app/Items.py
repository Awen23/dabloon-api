from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
import random

from app import app

from Users import abort_if_user_doesnt_exist
from config import client 

db = client.dabloons
collection = db.items

item_put_args = reqparse.RequestParser();
item_put_args.add_argument("user_details", type=str, help="User identifier is required", required=True);
item_put_args.add_argument("item_name", type=str, help="Item name is required", required=True);
item_put_args.add_argument("dabloons", type=int, help="Dabloons is required", required=True);
item_put_args.add_argument("link", type=str, help="Link is required", required=True);

item_update_args = reqparse.RequestParser();
item_update_args.add_argument("user_details", type=str, help="User identifier is required", required=True);
item_update_args.add_argument("item_id", type=str, help="Item ID is required", required=True);

def abort_if_item_doesnt_exist(market_id):
    if collection.find_one({"identifier": market_id}) is None:
        abort(404, message="Market doesn't exist")

@app.route('/items', methods=['PUT'])
def put(self, user_id):
    abort_if_user_doesnt_exist(user_id)
    args = item_put_args.parse_args()
    collection.insert_one({"identifier": user_id, "name": args["name"], "balance": args["balance"]})

@app.route('/items', methods=['GET'])
def get(self, user_id):
    abort_if_user_doesnt_exist(user_id)
    item = random.choice(collection.find({"sold": False}))
    return item

@app.route('/items', methods=['PATCH'])
def patch(self, item_id):
    abort_if_item_doesnt_exist(item_id)
    args = item_update_args.parse_args()
    collection.update_one({"identifier": args["item_id"]}, {"$set": {"sold": True, "buyer": args["user_identifier"]}})
        

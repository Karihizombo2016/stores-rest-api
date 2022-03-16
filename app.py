from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #This turn off the flask_sqlalchemy modification tracker
                                                    #the SQLAlchemy modification tracker is still running.
app.secret_key = 'miki'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity) #JWT creates a new end point /auth

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

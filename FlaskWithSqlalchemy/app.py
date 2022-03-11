from curses.ascii import US
from flask import Flask
from flask_restful import Api, Resource
import  urllib
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
# from flask_jwt import JWT

# from security import authenticate, identity

from resources.accesslevel_ex import AccessLevelList,GetAccessLevel

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@35.193.9.50/user_management'%urllib.parse.quote_plus('epos@123')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)
api = Api(app)


class User(Resource):
    def get(self):
        create_access=create_access_token(identity="saikat")
        return {"accesstoken":create_access}

api.add_resource(User,"/user")
api.add_resource(AccessLevelList,"/list")
api.add_resource(GetAccessLevel,"/list/<int:id>")

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    app.run(port=5000, debug=True)

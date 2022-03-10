from flask import Flask
from flask_restful import Api
import  urllib
# from flask_jwt import JWT

# from security import authenticate, identity

from resources.accesslevel_ex import AccessLevelList,GetAccessLevel

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@35.193.9.50/user_management'%urllib.parse.quote_plus('epos@123')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'jose'
api = Api(app)


# @app.before_first_request
# def create_tables():
#     db.create_all()


# jwt = JWT(app, authenticate, identity)  # /auth


api.add_resource(AccessLevelList,"/list")
api.add_resource(GetAccessLevel,"/list/<int:id>")

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    app.run(port=5000, debug=True)

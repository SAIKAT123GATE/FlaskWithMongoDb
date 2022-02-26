from flask import Flask,jsonify, request,redirect,url_for
from flask_cors import CORS
from flask_restful import Resource,Api
from flask_sqlalchemy import SQLAlchemy
from dataclasses import dataclass
import urllib
app=Flask('__name__')
api=Api(app)
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:%s@35.193.9.50/user_management'%urllib.parse.quote_plus('epos@123')

app.config['SQLALCHEMY_DATABASE_URI']=SQLALCHEMY_DATABASE_URI

db=SQLAlchemy(app)
print(SQLALCHEMY_DATABASE_URI)
print(db)

@dataclass
class AccessLevel(db.Model):
    __tablename__ = 'AccessLevel'
    AccessLevelId:int
    AccessLevelName:str

    AccessLevelId = db.Column(db.INTEGER, primary_key=True)
    AccessLevelName = db.Column(db.String(45), nullable=False)

    # def __repr__(self):
    #     return f"AccessLevelId : {self.AccessLevelId}, Name: {self.AccessLevelName}"

@dataclass
class User(db.Model):
    __tablename__ = 'User'
    UserId:int
    FirstName:str
    LastName:str
    Email:str
    UserId = db.Column(db.INTEGER, primary_key=True)
    FirstName = db.Column(db.String(200), nullable=False)
    LastName = db.Column(db.String(200))
    Email = db.Column(db.String(100), nullable=False)

class Hello(Resource):
    def get(self):
        return "Hello World"
class Access(Resource):
    def get(self):
        data=AccessLevel.query.all()
        print(data)
        output=data
        return jsonify({"status":"ok","data":data})
class Users(Resource):
    def get(self):
        data=User.query.all()
        return jsonify(data)
    def post(self):
        body=request.get_json();
        tempUser=User(FirstName=body['FirstName'],LastName=body['LastName'],Email=body['Email'])
        db.session.add(tempUser)
        db.session.commit()
        return redirect(url_for('users'))
        # return jsonify(body)


class ParticularUser(Resource):
    def get(self,Id):
        # data=db.session.query(User).filter(User.Email=="saikat@gmail.com").first()
        data=User.query.filter(User.Email=="saikat@gmail.com").first()
        return jsonify(data)


api.add_resource(Hello,"/")
api.add_resource(Access,"/access")
api.add_resource(Users,"/users")
api.add_resource(ParticularUser,"/user/<int:Id>")
if __name__=='__main__':
    app.run(debug=True)
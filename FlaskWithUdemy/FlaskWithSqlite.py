import json
from os import curdir
import sqlite3
from flask import Flask, jsonify
from flask_restful import Resource,Api,reqparse
connection=sqlite3.connect("./users.db",check_same_thread=False);
crsr = connection.cursor()
print("connected to database")

app=Flask('__name__')
api=Api(app)

class Person:
    TABLE_NAME = 'user'

    def __init__(self,id,username,password):
        self.id = id
        self.username = username
        self.password=password

class Home(Resource):
    def get(self):
        return {"status":"ok"}


class User(Resource):
    def get(self):
        # crsr.execute("SELECT * FROM user")
        crsr.execute("SELECT * FROM user WHERE id=1")
        data=crsr.fetchone();
        print("data=>",*data)
        if data:
            user=Person(*data);

            print("user=>",user.__dict__) #for json data serialize use __dict__
        return jsonify({"data":user.__dict__})

api.add_resource(Home,"/")
api.add_resource(User,"/user")
if __name__==("__main__"):
    app.run(port=3000,debug=True)

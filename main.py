from distutils.log import debug
import json
from flask import Flask,jsonify,request
from flask_restful import Resource,Api
from flask_cors import CORS
import pymongo
from bson.json_util import loads,dumps
from bson.objectid import ObjectId



connection_url="mongodb+srv://saikat:saikat123@cluster0.khele.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
app = Flask(__name__)
api=Api(app)

# GET THE DATABASE
client=pymongo.MongoClient(connection_url);
database=client.get_database("cruddata");
collection=database["users"];
class Hello(Resource):
    def get(self):
        return jsonify({"message":"Hi"})

    def post(self):

        data=request.get_json()
        print(data)
        return jsonify(data)
class ParticularData(Resource):
    def get(self,num):
        return jsonify({"num":num})

class UserData(Resource):
    def get(self):
        # query=json.loads(dumps(collection.find({})))
        query=collection.find({})
        # query2=collection.find({}).ObjectId
        # print(query);
        # print(query)
        output = {}
        i = 0
        for x in query:
            output[i] = x
            id=x.get('_id');
            print(id)
            output[i].pop('_id')
            output[i]['id']=str(id)
            i += 1
        # return jsonify({"status":"ok","data":query})
        return jsonify({"data":output})
    def post(self):
        data=request.get_json()
        print(data);
        query=collection.insert_one(data);
        print(query.inserted_id)
        return jsonify({"id":str(query.inserted_id)})

class ParticularUserData(Resource):
    def get(self,id):
        print(id)
        query=collection.find_one({"_id":ObjectId( id)})
        query.pop('_id')
        dict1=query

        dict1['id']=str(id)
        return jsonify({"status":"ok","data":dict1})

# Tradional way to do rest api with only flask
# @app.route("/")
# def hello_world():
#     return "Hello, World!"

api.add_resource(Hello,"/")
api.add_resource(ParticularData,"/data/<int:num>")
api.add_resource(UserData,"/userdata")
api.add_resource(ParticularUserData,"/user/<string:id>")


if __name__=='__main__':
    app.run(debug=True)
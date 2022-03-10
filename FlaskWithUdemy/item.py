import sqlite3
from flask import Flask, jsonify
from flask_restful import Resource,Api,reqparse
connection=sqlite3.connect("users.db",check_same_thread=False)
cursor=connection.cursor();

class Items(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self):
        getallitems=self.getAllItem()
        print("getAllitems=>",getallitems);
        if getallitems:
            return getallitems
        else:
            return {"message":"Not found anything"}

    @classmethod
    def getAllItem(cls):
        query="SELECT * FROM items"
        result=cursor.execute(query)
        data=result.fetchall();
        connection.close()
        print("data",data);
        item=[];
        if data:
            for row in data:
                item.append({"id":row[0],"name":row[1],"price":row[2]})
            return {"data":item}
from ast import parse
from email import parser
from flask import Flask, jsonify
from flask_restful import Resource,Api,reqparse

app=Flask('__name__')
api=Api(app)


items=[
    {
        "name":"item1",
        "price":10.11
    }
]
class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    def get(self,name):

        data=next(filter(lambda item:item['name']==name,items),None)

        return data
        # for item in items:
        #     if item['name']==name:
        #         return item
        # return {"item":None},404
    def post(self,name):
        data=Item.parser.parse_args();
        print(data)
        item={"name":name,"price":12}
        items.append(item)
        return items,201

api.add_resource(Item,"/item/<string:name>")

if __name__=='__main__':
    app.run(port=3000,debug=True)
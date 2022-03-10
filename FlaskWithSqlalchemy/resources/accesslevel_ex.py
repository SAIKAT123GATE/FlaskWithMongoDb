from flask import Flask
from flask_restful import Resource,Api
from models.accesslevel import AccessLevelModel


class AccessLevelList(Resource):
    def get(self):
        data=AccessLevelModel.query.all();
        items=[];
        for d in data:
            items.append(d.json())
        print(items)
        return {"status":"okay","items":items}
class GetAccessLevel(Resource):
    def get(self,id):
        print(id)
        data=AccessLevelModel.query.filter(AccessLevelModel.AccessLevelId==id).first()
        print(data)

        if data:
            return{"status":"okay","data":data.json()}
        else:
            return None
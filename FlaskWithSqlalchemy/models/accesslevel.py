
from db import db

class AccessLevelModel(db.Model):
    __tablename__ = 'AccessLevel'

    AccessLevelId:int
    AccessLevelName:str
    AccessLevelId = db.Column(db.Integer, primary_key=True)
    AccessLevelName = db.Column(db.String(45), nullable=False)

    def __init__(self,AccessLevelName):
        self.AccessLevelName=AccessLevelName

    def json(self):
        return {"AccessLevelId":self.AccessLevelId,"AccessLevelName":self.AccessLevelName}

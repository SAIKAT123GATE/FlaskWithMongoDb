class Person():
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def __repr__(self):
        return 'name:{},id:{}'.format(self.name,self.id)

bob=Person("Bob",1)
print(bob)
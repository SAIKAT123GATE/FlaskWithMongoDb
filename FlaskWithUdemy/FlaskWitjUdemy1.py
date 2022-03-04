from crypt import methods
from flask import Flask, jsonify, request
app = Flask('__name__')


stores = [
    {
        "name": "store1",
        "items": [{"price": 18, "name": "My Item"}]
    },
    {
        "name": "store2",
        "items": []
    }

]

#home route for testing api is running
@app.route("/")
def home():

    return {"status": "ok"}

#get all stores data
@app.route("/allstore")
def allStore():
    return jsonify({"status": "Okay", "data": stores})

#save a particular store
@app.route("/store", methods=['POST'])
def saveAStore():
    data=request.get_json();
    print(data)
    stores.append(data);
    return jsonify(stores);

# get a particular store by it's name


@app.route('/store/<string:name>')
def getAStoreByName(name):
    for store in stores:
        if(store['name'] == name):
            return jsonify(store)
    return jsonify({"message": "{} not found".format(name)})



#get a particular store item by store name
@app.route("/store/<string:name>/item")

def getItem(name):
    for store in stores:
        if(store['name']==name):
            return jsonify(store['items'])
    return jsonify({"message":"store not found"})

@app.route("/store/<string:name>/item",methods=['POST'])
def storeItem(name):
    data=request.get_json()

    for store in stores:
        if(store['name']==name):
            store["items"].append(data)
            return jsonify(store)
    return jsonify({"message":"store not found"})

if __name__ == '__main__':
    app.run(port=3000, debug=True)

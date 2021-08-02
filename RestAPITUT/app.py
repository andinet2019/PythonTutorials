import json
from flask import Flask,jsonify,request
app=Flask(__name__)
app.config["DEBUG"]= True
@app.route('/')
def index():
    return jsonify({'name': 'alice',
                       'email': 'alice@outlook.com'})
@app.route('/records/<str:name>')
def query_records(name):
    name= request.args.get('name')
    print(name)
app.run()
# {"name": "alice", "email": "alice@outlook.com"}
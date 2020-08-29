from flask import Flask, request, make_response, jsonify
from Backend.CouchDB import CouchDBHandler as ha
from Backend.CouchDB import auth_user as auth
from Backend.CouchDB import create_account as create
from Backend.CouchDB import auth_user_by_id as auth_id
from Backend.CouchDB import reset_password as reset_PSW
import json


url = "127.0.0.1"
username = 'admin'
password = 'password'

handler = ha(url, username, password)
# users = handler.Server['staff']
# print(users['0e2873e20cda84963a1e60b5360011b5'])

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    try:
        error = str(error)
        return make_response({error:'Bad request'}, 400)
    except:
        return make_response({'error':'Bad request'}, 400)

@app.errorhandler(404)
def not_found(error):
    try:
        error = str(error)
        return make_response({error: 'Resource not found'}, 400)
    except:
        return make_response({'error': 'Resource not found'}, 400)

@app.route('/login', methods=["POST"])
def auth_user():
    print('in the login')
    rawData = request.data.decode('utf-8')
    print(rawData)
    print(len(rawData))
    try:
        data = json.loads(rawData)
        loginUsername = data['username']
        loginPassword = data['password']
        staffDB = handler.Server['staff']
        result = auth(staffDB, loginUsername, loginPassword)
        if result['auth_result']:
            return jsonify({'result': 'Okay', 'user': loginUsername, "userid": result['userid'], 'userTitle': result['title']})
        else:
            return jsonify({'result': 'False'})

    except Exception as e:
        print("in exception")
        print(e)
        return jsonify({'result':'error'})
        # bad_request("data cannot be read")

@app.route('/signup', methods=["POST"])
def sign_up():
    try:
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)
        print(data)
        createUseranme = data['username']
        createPassword = data['password']
        createTitle = data['title']
        staffDB = handler.Server['staff']
        if create(staffDB, createUseranme, createPassword, createTitle):
            return jsonify({'result': 'Okay'})
        else:
            return jsonify({"result": 'Create failed'})
    except:
        bad_request("data cannot be read")

@app.route('/authPSW', methods=['POST'])
def auth_user_by_id():
    try:
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)
        userId = data['userId']
        oldPassword = data['password']
        staffDB = handler.Server['staff']
        if auth_id(staffDB, userId, oldPassword):
            return jsonify({'result': 'Okay'})
        else:
            return jsonify({'result': 'Old password wrong'})
    except:
        bad_request("wrong password")

@app.route('/resetPSW', methods=['POST'])
def reset_password():
    try:
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)
        userId = data['userId']
        newPassword = data['password']
        staffDB = handler.Server['staff']
        if reset_PSW(staffDB, userId, newPassword):
            return jsonify({"result": 'Okay'})
        else:
            return jsonify({'result': 'fail to reset'})
    except:
        bad_request("fail to reset")

if __name__ == '__main__':
    app.run(host='127.0.0.1' ,port="4000")

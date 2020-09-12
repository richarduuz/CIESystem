from flask import Flask, request, make_response, jsonify, abort
from Backend.CouchDB import CouchDBHandler as ha
from Backend.CouchDB import auth_user as auth
from Backend.CouchDB import create_account as create
from Backend.CouchDB import auth_user_by_id as auth_id
from Backend.CouchDB import reset_password as reset_PSW
from Backend.CouchDB import reset_other_password as reset_OPSW
from Backend.CouchDB import delete_account as delete_a
from Backend.CouchDB import create_new_quo as create_quo
from werkzeug.exceptions import BadRequest
import json
import pandas
import Backend.util as util


url = "127.0.0.1"
username = 'admin'
password = 'password'

handler = ha(url, username, password)
# users = handler.Server['staff']
# print(users['0e2873e20cda84963a1e60b5360011b5'])

app = Flask(__name__)

@app.errorhandler(400)
def bad_request(error):
    abort(400, error)

@app.errorhandler(404)
def not_found(error):
    abort(404, error)

@app.route('/login', methods=["POST"])
def auth_user():
    print('in the login')
    rawData = request.data.decode('utf-8')
    try:
        data = json.loads(rawData)
        loginUsername = data['username']
        loginPassword = data['password']
        staffDB = handler.Server['staff']
        result = auth(staffDB, loginUsername, loginPassword)
        if result['auth_result']:
            return jsonify({'result': 'Okay', 'username': loginUsername, "userid": result['userid'], 'userTitle': result['title']})
        else:
            return jsonify({'result': 'False'})
    except Exception as e:
        return jsonify({'result':'error'})

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
        result =  create(staffDB, createUseranme, createPassword, createTitle)
        if result['result']:
            return jsonify({'result': 'Okay'})
        else:
            return jsonify({"result": 'Create failed', 'reason': result['reason']})
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
    except Exception as e:
        bad_request(str(e))

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
    except Exception as e:
        bad_request(str(e))

@app.route('/resetOtherPSW', methods=['POST'])
def reset_other_password():
    try:
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)
        username = data['username']
        password = data['password']
        staffDB = handler.Server['staff']
        if reset_OPSW(staffDB, username, password):
            return jsonify({"result": "Okay"})
        else:
            return jsonify({"result": "fail to reset"})
    except Exception as e:
        bad_request(str(e))

@app.route('/deleteAccount', methods=['POST'])
def delete_account():
    try:
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)
        username = data['username']
        staffDB = handler.Server['staff']
        result = delete_a(staffDB, username)
        if result['result']:
            return jsonify({"result": "Okay"})
        else:
            return jsonify({'result': 'failed to delete', 'reason': result['reason']})
    except Exception as e:
        bad_request(str(e))

@app.route('/extractQuotation', methods=['POST'])
def extractQuo():
    try:
        print('in the extraction')
        file = request.files
        filename = ""
        for i in file:
            filename = i
            break
        file = file.get(filename)
        df = pandas.read_excel(file, sheet_name="Sheet1")
        result = util.extractQuo(df)
        if result['status'] != "Okay":
            raise Exception(result['message'])
        return jsonify(result)
    except Exception as e:
        bad_request(str(e))

@app.route('/confirmQuotation', methods=['POST'])
def confrimQuo():
    try:
        print("in confirm")
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)
        quoDB = handler.Server['quotation']
        result = create_quo(quoDB, data)
        print(result)
        return jsonify({'result':'okay'})
    except Exception as e:
        bad_request(str(e))




if __name__ == '__main__':
    app.run(host='127.0.0.1' ,port="4000")


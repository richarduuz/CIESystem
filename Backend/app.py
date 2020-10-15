from flask import Flask, request, make_response, jsonify, abort
from Backend.CouchDB import CouchDBHandler as ha
from Backend.CouchDB import auth_user as auth
from Backend.CouchDB import create_account as create
from Backend.CouchDB import auth_user_by_id as auth_id
from Backend.CouchDB import reset_password as reset_PSW
from Backend.CouchDB import reset_other_password as reset_OPSW
from Backend.CouchDB import delete_account as delete_a
from Backend.CouchDB import create_new_quo as create_quo
from Backend.CouchDB import getUncompletedForms, getUncompletedRFQ, confirm_quo_price, getPendingForms, confirm_rfq_price
import json
import pandas
import Backend.util as util

app = Flask(__name__)
app.config.from_pyfile('settings.py')

url = app.config['COUCHDB_URL']
username = app.config['COUCHDB_NAME']
password = app.config['COUCHDB_PASSWORD']
host = app.config['HOST']
port = app.config['PORT']

handler = ha(url, username, password)

@app.errorhandler(400)
def bad_request(error):
    return str(error), 400

@app.errorhandler(404)
def not_found(error):
    return str(error), 404

@app.errorhandler(500)
def internal_error(error):
    return str(error), 500

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
def confirmQuo():
    try:
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)
        quoDB = handler.Server['quotation']
        result = create_quo(quoDB, data)
        return jsonify({'result':'Okay'})
    except Exception as e:
        bad_request(str(e))

@app.route('/uncompletedForms', methods=['GET'])
def uncompletedForms():
    try:
        quoDB = handler.Server['quotation']
        result = getUncompletedForms(quoDB)
        result = {'status': 'Okay', 'body': result}
        return jsonify(result)
    except Exception as e:
        bad_request(str(e))

@app.route('/uncompletedRFQ/<userId>', methods=['GET'])
def uncompleteRFQ(userId):
    try:
        rfqDB = handler.Server['request_for_quotation']
        result = getUncompletedRFQ(rfqDB, userId)
        result = {'status': 'Okay', 'body': result}
        return jsonify(result)
    except Exception as e:
        internal_error(str(e))

@app.route('/pendingForms', methods=['GET'])
def pendingforms():
    try:
        quoDB = handler.Server['quotation']
        result = getPendingForms(quoDB)
        result = {'status': 'Okay', 'body': result}
        print(result)
        return jsonify(result)
    except Exception as e:
        bad_request(str(e))

@app.route('/confirmQuotationPrice', methods=['POST'])
def confirmQuoPrice():
    try:
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)
        quoDB = handler.Server['quotation']
        result = confirm_quo_price(quoDB, data)
        if result['status'] == 'Okay':
            return jsonify({'status':'Okay', 'message': "已录入数据库"})
        else:
            return jsonify({'status': 'Error','message': result['message']})
    except Exception as e:
        bad_request(str(e))

@app.route('/confirmRFQ', methods=["POST"])
def confirmRFQ():
    try:
        rawData = request.data.decode('utf-8')
        data = json.loads(rawData)
        quoDb = handler.Server['quotation']
        rfqDb = handler.Server['request_for_quotation']
        result = confirm_rfq_price(quoDb, rfqDb, data)
        if result['status'] == "Okay":
            return jsonify({'status': 'Okay', 'message': "已录入数据库"})
        else:
            return jsonify({'status': 'Error', 'message': result['message']})
    except Exception as e:
        bad_request(str(e))

if __name__ == '__main__':
    app.run(host=host ,port=port)


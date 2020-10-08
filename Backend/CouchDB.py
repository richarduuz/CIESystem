import couchdb
from datetime import datetime

class CouchDBHandler:
    Username = ""
    Password = ""
    Server = None
    URL = ""
    Port = "5984"
    Status = True
    QuotationDB = None
    RFQDB = None
    UserDB = None

    def __init__(self, url, username, password):
        address = "http://{admin}:{password}@{url}:{port}"
        self.Username = username
        self.Password = password
        self.URL = url
        try:
            self.Server = couchdb.Server(address.format(admin = self.Username, password = self.Password, url = self.URL, port = self.Port))
        except:
            self.Status = False

def auth_user(db, username, password):
    flag = False
    data = {'auth_result': False}
    for doc in db:
        if db[doc].get('username')==username and db[doc].get('password')==password:
            data = {'auth_result': True, 'userid': db[doc].get('_id'), 'title': db[doc].get('title')}
            flag = True
            break
    return data

def create_account(db, username, password, title):
    staffNames = [db[doc].get('username') for doc in db]
    if username in staffNames:
        return {'result': False, 'reason': 'This username has existed'}
    if len(username) == 0 or len(password) == 0 or title not in ['Buyer', 'Sales']:
        return {'result': False, 'reason': 'Invalid username, password, or title'}
    doc = {'username': username, 'password': password, 'title': title}
    try:
        db.save(doc)
        return {'result': True}
    except:
        return {'result': False, 'reason': 'Unknown error'}

def auth_user_by_id(db, userId, password):
    result = False
    if userId in db:
        if password == db[userId].get('password'):
            result = True
    return result

def reset_password(db, userId, password):
    result = False
    if userId in db:
        doc = db.get(userId)
        doc['password'] = password
        db.save(doc)
        result = True
    return result

def reset_other_password(db, username, password):
    result = False
    userId = get_id_from_username(db, username)
    if len(userId) != 0:
        if reset_password(db, userId, password):
            result = True
    return result

def delete_account(db, username):
    result = {'result': False}
    userId = get_id_from_username(db, username)
    if len(userId) != 0:
        db.delete(db[userId])
        result['result'] = True
    else:
        result['reason'] = "user does not exist"
    return result

def create_new_quo(db, quo):
    #TODO send data to couchDB and save them
    entries = quo['body']
    username = quo['username']
    userTitle = quo['userTitle']
    for item in entries:
        item['询价日期'] = datetime.now().strftime('%Y.%m.%d %H:%M')
        if userTitle == 'Sales':
            item['销售'] = username
        item['目前状态'] = "等待采购回复"
        db.save(item)
    return {"result": "Okay"}

def getUncompletedForms(db):
    result = []
    for doc in db:
        tmp = dict(db[doc])
        if tmp['目前状态'] == '等待采购回复':
            tmp['quoId'] = doc
            result.append(tmp)
    return result

def getPendingForms(db):
    result = []
    for doc in db:
        tmp = dict(db[doc])
        if tmp['目前状态'] == '采购已回复':
            tmp['quoId'] = doc
            result.append(tmp)
    return result

def confirm_quo_price(db, quo):
    result = {"status": "Okay"}
    try:
        entries = quo['body']
        username = quo['username']
        userTitle = quo['userTitle']
        for quoId in entries.keys():
            if quoId in db:
                doc = db.get(quoId)
                doc['实际回复日期'] = datetime.now().strftime('%Y.%m.%d %H:%M')
                if userTitle == 'Buyer':
                    doc['采购'] = username
                doc['目前状态'] = '采购已回复'
                for key in entries[quoId].keys():
                    doc[key] = entries[quoId][key]
                db.save(doc)
    except Exception as e:
        result['status'] = "Error"
        result['message'] = str(e)
    finally:
        return result

def confirm_rfq_price(quoDb, rfqDb, payload):
    result = {'status': "Okay"}
    try:
        quoId = payload['quoId']
        body = payload['body']
        timestamp = datetime.now().strftime('%Y.%m.%d %H:%M')
        tmpRFQ = {'采购': payload['username'], "回复日期": timestamp, "回复内容": body, 'quoId': quoId, 'userId': payload['userId']}
        rfqDb.save(tmpRFQ)
    except Exception as e:
        result['status'] = "Error"
        result['message'] = str(e)
    finally:
        return result
















def get_id_from_username(db, username):
    userId = ""
    staffNames = [(db[doc].get('username'), doc) for doc in db]
    for item in staffNames:
        if username in item:
            userId = item[1]
            break
    return userId










import couchdb

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
    if len(username) == 0 or len(password) == 0 or title not in ['Buyer', 'Sales']:
        return False
    doc = {'username': username, 'password': password, 'title': title}
    try:
        db.save(doc)
        return True
    except:
        return False

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









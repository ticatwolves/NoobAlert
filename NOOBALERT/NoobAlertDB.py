from pymongo import MongoClient
from bson.objectid import ObjectId
import time

#Connection to MongoDB
conn = MongoClient()

#Creating MoviesDB Database
noobalertuserref = conn.NoobAlertDB


def uid(username):
    ref = noobalertuserref['USERS']
    d = ref.find({'Username': username},{'_id':1})
    print(d)
    for p in d:
        print(p)
        uid = (p['_id'])
        return uid

def checkavability(username):
    check = uid(username)
    if not check:
        return True
    else:
        return False

#checkavability('Raymon Batsy')

def addUsers(username,password,email):
    ref = noobalertuserref['USERS']
    ref.insert({
        'Username':username,
        'password':password,
        'email':email
    })

#addUsers('Raymon tsy',"Kmd",'fbfd')

def getloginDetails(username):
    ref = noobalertuserref['USERS']
    d = ref.find({'Username':username})
    for p in d:
        return p['password']

def addmsg(username,msg):
    _id = uid(username)
    myref = noobalertuserref['Messages'][_id]
    myref.insert({
        'Message': msg,
    })

#addmsg('Raymon Batsy',"Noob fuck you")

def showmessage(username):
    _id = uid(username)
    myref = noobalertuserref['Messages'][_id]
    ms = myref.find()
    msg=[]
    for d in ms:
        msg.append(d['Message'])
    return msg
#showmessage('Raymon Batsy')
"""def deleteComments(m_id,c_id):
#    ref = comments_db[m_id]
    ref.delete_many({'_id':ObjectId(c_id)})
    print("Deleted")
"""


#print("Done")

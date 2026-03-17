import firebase_admin
from firebase_admin import credentials, db

if not firebase_admin._apps:

    cred = credentials.Certificate("serviceAccountKey.json")

    firebase_admin.initialize_app(cred,{
        "databaseURL":"https://smart-home-ai-6aed5-default-rtdb.firebaseio.com/"
    })


def get_database():

    return db.reference("/")
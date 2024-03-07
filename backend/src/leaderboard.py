from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)

# Initialize Firebase
load_dotenv()

# Initialize Firebase with credentials from environment variable
cred = credentials.Certificate('jokerker-d9272-firebase-adminsdk-sbyd5-fda51193ba.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
easyLeaderboard_ref = db.collection('EasyLeaderboard')
normalLeaderboard_ref = db.collection('NormalLeaderboard')
hardLeaderboard_ref = db.collection('HardLeaderboard')

def get_easyLeaderboard_data():
    docs = easyLeaderboard_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

@app.route('/getEasyLeaderboard', methods=['GET'])
def getEasyGames():
    return jsonify(get_easyLeaderboard_data())
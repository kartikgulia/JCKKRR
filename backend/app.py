
from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)

# Initialize Firebase
load_dotenv()

# Initialize Firebase with credentials from environment variable
cred = credentials.Certificate('jokerker-d9272-firebase-adminsdk-sbyd5-fda51193ba.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
EasyGames_ref = db.collection('EasyGames')
EasyRounds_ref = db.collection('EasyRounds')
images_ref = db.collection('images')
easyleaderboard_ref = db.collection('Easyleaderboard')
normalleaderboard_ref = db.collection('NormalLeaderboard')
hardleaderboard_ref = db.collection('Hardleaderboard')
players_ref = db.collection('players')


# Function to retrieve data from Firestore
def get_EasyGames_ref_data():
    docs = EasyGames_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

def get_EasyRounds_ref_data():
    docs = EasyRounds_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

def get_images_data():
    docs = images_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict


def get_easy_leaderboard_data():
    docs = easyleaderboard_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

def get_normal_leaderboard_data():
    docs = normalleaderboard_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

def get_hard_leaderboard_data():
    docs = hardleaderboard_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

def get_players_data():
    docs = players_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

@app.route('/getEasyGames', methods=['GET'])
def getEasyGames():
    print(get_EasyGames_ref_data())

@app.route('/getEasyRounds', methods=['GET'])
def getEasyRounds():
    print(get_EasyRounds_ref_data())

@app.route('/getImages', methods=['GET'])
def getImages():
    print(get_images_data())

@app.route('/getEasyLeaderboard', methods=['GET'])
def getEasyLeaderboard():
    print(get_easy_leaderboard_data())

@app.route('/getNomralLeaderboard', methods=['GET'])
def getNormalLeaderboard():
    print(get_normal_leaderboard_data())

@app.route('/getHardLeaderboard', methods=['GET'])
def getHardLeaderboard():
    print(get_hard_leaderboard_data())

@app.route('/getPlayers', methods=['GET'])
def getPlayers():
    print(get_players_data())

    
@app.route('/signin', methods=['POST'])
def signin():
    # THIS IS JUST AN EXAMPLE. WE SHOULD NOT HAVE VALIDATION HERE. IT SHOULD BE ANOTHER FUNCTION IN ANOTHER FILE.
    # We would just call it here. This example is just to show u guys how everything works.
    
    # Extract the username and password from the request
    data = request.json
    username = data.get('username')
    password = data.get('password')

    print("Hi Ryan")
    if username == "admin" and password == "password":
        return jsonify({"message": "Successfully signed in"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@app.route('/images', methods=['GET'])
def get_images():
    images_data = get_images_data()
    return jsonify(images_data)

@app.route('/easyleaderboard', methods=['GET'])
def get_easyleaderboard():
    easyleaderboard_data = get_easy_leaderboard_data()
    return jsonify(easyleaderboard_data)

@app.route('/normalleaderboard', methods=['GET'])
def get_normalleaderboard():
    normalleaderboard_data = get_normal_leaderboard_data()
    return jsonify(normalleaderboard_data)

@app.route('/hardleaderboard', methods=['GET'])
def get_hardleaderboard():
    hardleaderboard_data = get_hard_leaderboard_data()
    return jsonify(hardleaderboard_data)

@app.route('/easyGames', methods=['GET'])
def get_easyGames():
    easyGames_data = getEasyGames()
    return jsonify(easyGames_data)

@app.route('/easyRounds', methods=['GET'])
def get_easyRounds():
    easyRounds_data = getEasyRounds()
    return jsonify(easyRounds_data)

@app.route('/players', methods=['GET'])
def get_players():
    players_data = get_players_data()
    return jsonify(players_data)


if __name__ == '__main__':
    app.run(port=5000)

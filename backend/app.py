
import os
import random
from io import BytesIO

import firebase_admin
import requests
from dotenv import load_dotenv
from firebase_admin import credentials, firestore
from flask import Flask, jsonify, request
from flask_cors import CORS
from PIL import Image
from Round import BackgroundImage, Round

app = Flask(__name__)
CORS(app)

# Initialize Firebase
load_dotenv()

# Initialize Firebase with credentials from environment variable
cred = credentials.Certificate(
    'jokerker-d9272-firebase-adminsdk-sbyd5-fda51193ba.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
EasyGames_ref = db.collection('EasyGames')
EasyRounds_ref = db.collection('EasyRounds')
MediumGames_ref = db.collection('MediumGames')
MediumRounds_ref = db.collection('MediumRounds')
HardGames_ref = db.collection('HardGames')
HardRounds_ref = db.collection('HardRounds')
images_ref = db.collection('images')
leaderboard_ref = db.collection('leaderboard')
players_ref = db.collection('players')


# Gets random image from image collection and sends target, background, date and target coordinates to one of the rounds
def get_TargetBgImages(difficulty, i):
    image_data = get_randImage()
    backgroundImage = image_data['url']
    im = Image.open(image_data['url'])
    width, height = im.size
    dateTaken = image_data["datetaken"]  # got date from json
    dateTaken = dateTaken[0:4]
    # not sure if we need to store background's corner coordinates, just need it for finding target's corner coordinates
    if (difficulty == "MediumRounds"):
        TL = (random.randint(1, width-20), random.randint(1, height-20))
        TR = TL + (20, 0)
        BL = TL + (0, 20)
        BR = TL + (20, 20)
    elif (difficulty == "EasyRounds"):
        TL = (random.randint(1, width-20), random.randint(1, height-20))
        TR = TL + (40, 0)
        BL = TL + (0, 40)
        BR = TL + (40, 40)
    else:
        TL = (random.randint(1, width-20), random.randint(1, height-20))
        TR = TL + (10, 0)
        BL = TL + (0, 10)
        BR = TL + (10, 10)
    
    # backgroundImage.show()
    data = {  # most of the data is not needed for rounds, ideally we just need dates, filepaths for background and target, and target's corner coordinates
        "id": image_data['id'],
        "url": backgroundImage,
        "TL": TL,
        "TR": TR,
        "BL": BL,
        "BR": BR,
        "date": dateTaken
    }
    # sends data to one of the collections for rounds
    # difficulty -> EasyRounds, MediumRounds, HardRounds, i -> round number
    doc_ref = db.collection(difficulty).document(i)
    doc_ref.set(data)


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


def get_randImage():
    docs = images_ref.get()
    documents_list = [doc.to_dict() for doc in docs]
    if documents_list:
        random_image_data = random.choice(documents_list)
        return random_image_data
    else:
        return None


def get_leaderboard_data():
    docs = leaderboard_ref.get()
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


@app.route('/getLeaderboard', methods=['GET'])
def getLeaderboard():
    print(get_leaderboard_data())


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


@app.route('/rand_image', methods=['GET'])
def get_randImages():
    image_data = get_randImage()
    return jsonify(image_data)


# @app.route('/bg_target', methods=['GET'])

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    leaderboard_data = get_leaderboard_data()
    return jsonify(leaderboard_data)


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

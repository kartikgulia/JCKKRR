from io import BytesIO

from dotenv import load_dotenv
from FirebaseAccess.firebase import db
from flask import Flask, jsonify, request
from flask_cors import CORS
from GameModule.gameCreationFunctions import createGameForPlayer
from GameModule.GameInterface import Game
from UserModule.Player import Player
from UserModule.PlayerSessionManager import PlayerSessionManager

app = Flask(__name__)
CORS(app)

# Initialize Firebase
load_dotenv()

# Initialize Firebase with credentials from environment variable
EasyGames_ref = db.collection('EasyGames')
EasyRounds_ref = db.collection('EasyRounds')
MediumGames_ref = db.collection('MediumGames')
MediumRounds_ref = db.collection('MediumRounds')
HardGames_ref = db.collection('HardGames')
HardRounds_ref = db.collection('HardRounds')

easyleaderboard_ref = db.collection('EasyLeaderboard')
mediumleaderboard_ref = db.collection('MediumLeaderboard')
hardleaderboard_ref = db.collection('HardLeaderboard')
players_ref = db.collection('players')


def get_easy_leaderboard_data():
    docs = easyleaderboard_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict


def get_medium_leaderboard_data():
    docs = mediumleaderboard_ref.get()
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


@app.route('/signin', methods=['POST'])
def signin():

    data = request.json
    username = data.get('username')
    password = data.get('password')

    print("Hi Ryan")
    if username == "admin" and password == "password":
        return jsonify({"message": "Successfully signed in"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


# Active player sessions

playerManager: PlayerSessionManager = PlayerSessionManager()  # SINGLETON
userID: str = "bo3bw4GUJdFhTp6aEqiD"
tempPlayer: Player = Player(userID=userID)
tempPlayer.name = "Rayyan"
tempPlayer.gameIDsPlayed = ["EasyGame1"]
playerManager.addPlayer(userID, tempPlayer)


@app.route('/getGameInfo', methods=['GET'])
# This route does the following:
# 1) Creates a Game Object for the currentPlayer
# 2) Sets the game ID of the game they're going to play
# 3) Calls the startGame() function which uses the game ID to get game information from the database, save the array of Round objects dictionary to Game Object, and return the information
def getGameInfo():

    data = request.json

    gameDifficultyLevel: str = data['gameDifficultyLevel']
    userID: str = data['userID']

    # temp for testing
    userID: str = "bo3bw4GUJdFhTp6aEqiD"

    currentPlayer: Player = playerManager.getPlayer(playerID=userID)

    # Sets the Game ID for the game object

    createGameForPlayer(currentPlayer, gameDifficultyLevel)

    if currentPlayer.currentGame != None:
        print(f"Created {gameDifficultyLevel} game for {currentPlayer.name}")

        # Now go to the Game Interface and complete the startGame function

        # Call startGame() which returns the game info
        arrayOfRoundDictionaries = currentPlayer.currentGame.startGame()

        # Need to return the JSONIFY of game info
        return jsonify({"message": "Yay", "gamesArray": arrayOfRoundDictionaries})

    else:
        print(
            f"Could not create {gameDifficultyLevel} game for {currentPlayer.name}")

        return jsonify({"message": "No more games left"})


@app.route('/easyleaderboard', methods=['GET'])
def get_easyleaderboard():
    easyleaderboard_data = get_easy_leaderboard_data()
    return jsonify(easyleaderboard_data)


@app.route('/mediumleaderboard', methods=['GET'])
def get_mediumleaderboard():
    mediumleaderboard_data = get_medium_leaderboard_data()
    return jsonify(mediumleaderboard_data)


@app.route('/hardleaderboard', methods=['GET'])
def get_hardleaderboard():
    hardleaderboard_data = get_hard_leaderboard_data()
    return jsonify(hardleaderboard_data)


if __name__ == '__main__':
    app.run(port=5000)


# Below this are just example functions. They are not part of the application.


# Example Functions using firebase
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


# @app.route('/getImages', methods=['GET'])
# def getImages():
#     print(get_images_data())


@app.route('/getEasyLeaderboard', methods=['GET'])
def getEasyLeaderboard():
    print(get_easy_leaderboard_data())


@app.route('/getMediumLeaderboard', methods=['GET'])
def getMediumLeaderboard():
    print(get_medium_leaderboard_data())


@app.route('/getHardLeaderboard', methods=['GET'])
def getHardLeaderboard():
    print(get_hard_leaderboard_data())


@app.route('/getPlayers', methods=['GET'])
def getPlayers():
    print(get_players_data())


# @app.route('/images', methods=['GET'])
# def get_images():
#     images_data = get_images_data()
#     return jsonify(images_data)


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

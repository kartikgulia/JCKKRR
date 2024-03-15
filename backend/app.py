import random
from io import BytesIO

from dotenv import load_dotenv
from FirebaseAccess.firebase import auth, db
from flask import Flask, jsonify, request
from flask_cors import CORS
from GameModule.gameCreationFunctions import createGameForPlayer
from GameModule.GameInterface import Game
from UserModule.Player import Player
from UserModule.PlayerSessionManager import PlayerSessionManager

app = Flask(__name__)
CORS(app)


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


# Active player sessions

playerManager: PlayerSessionManager = PlayerSessionManager()  # SINGLETON
userID: str = "bo3bw4GUJdFhTp6aEqiD"
tempPlayer: Player = Player(userID=userID)
tempPlayer.name = "Rayyan"
tempPlayer.gameIDsPlayed = ["EasyGame1"]
playerManager.addPlayer(userID, tempPlayer)


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
    email = data.get('email')
    password = data.get('password')
    try:

        # Authenticate the user with the provided email and password
        user = auth.sign_in_with_email_and_password(email, password)

        # if the auth is successful
        user_token = user['localId']

        # If the uid exists

        if playerManager.getPlayer(user_token) != None:
            return jsonify({"message": "Successfully logged in", "token": user_token}), 200

        # If the uid does not exist
        # Add the uid to active player session
        else:
            playerObject: Player = Player(userID=user_token)
            playerObject.name = email

            # playerDoc  = db.collection('players').document(user_token).get()
            # playerObject.gameIDsPlayed = playerDoc.to_dict()["gamesPlayed"]
            playerManager.addPlayer(user_token, playerObject)

        return jsonify({"message": "Successfully logged in", "token": user_token}), 200
    except Exception as e:
        # Handle exceptions (e.g., user not found, wrong password, etc.)
        error_message = str(e)
        return jsonify({"message": error_message}), 401


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        data = request.json
        username = data.get('username').strip()
        email = data.get('email')
        password = data.get('password')

        # Check if username is already taken

        players_ref = db.collection('players')

        isUniqueUsername = True

        for doc in players_ref.stream():

            player_data = doc.to_dict()

            if player_data['name'] == username:
                isUniqueUsername = False
                break

        if not isUniqueUsername:
            return jsonify({"message": "Username taken. Try something else"}), 401

        try:

            user = auth.create_user_with_email_and_password(email, password)
            uid = user['localId']
            data = {
                'name': f'{username}',
                'email': f'{email}',
                'EasyScore': 0,
                "MediumScore": 0,
                "HardScore": 0,
                'playerid': uid,
                'gamesPlayed': []
            }

            db.collection('players').document(uid).set(data)
            print('Player added to Firestore.')

            return jsonify({"message": "Successfully signed up"}), 200
        except Exception as e:

            error_message = str(e)
            return jsonify({"message": error_message}), 401


@app.route('/getProfileInfo', methods=["GET"])

def getProfileInfo():

    userID = request.args.get('userID')

    

    try:

        currentPlayer : Player = playerManager.getPlayer(playerID=userID)

        currentPlayer.updateInfo()
    
        name = currentPlayer.name
        email = currentPlayer.email
        easyScore = currentPlayer.easyScore
        mediumScore = currentPlayer.mediumScore
        hardScore = currentPlayer.hardScore

        return jsonify({"message" : "Success", "name" : name, "email": email, "easyScore" : easyScore, "mediumScore":mediumScore, "hardScore" : hardScore}), 200

    
    except Exception as e:
        return jsonify({"message" : "Failed", "description": f"{e}"}), 401
    






@app.route('/getExistingGameInfo', methods=['GET'])
def getExistingGameInfo():

    userID = request.args.get('userID')

    currentPlayer = playerManager.getPlayer(playerID=userID)

    currentPlayer.updateInfo()

    # Check if they have an existing game

    currentGame: Game = currentPlayer.currentGame

    try:

        if currentGame == None:
            return jsonify({"message": "Success", "description": f"No existing game"}), 200

        # Player has a current game

        arrayOfRoundDictionaries = currentGame.getArrayOfRoundDictionaries()
        currentRoundNumber = currentGame.currentRoundNumber
        difficulty = currentGame.difficulty

        return jsonify({"message": "Success", "description": f"Game exists", "roundsArray": arrayOfRoundDictionaries, "currentRoundNumber": currentRoundNumber, "difficulty": difficulty}), 200

    except Exception as e:
        return jsonify({"message": "Failed", "description": f"{e}"}), 401


# This route does the following:
# 1) Creates a Game Object for the currentPlayer
# 2) Sets the game ID of the game they're going to play
# 3) Calls the startGame() function which uses the game ID to get game information from the database, save the array of Round objects dictionary to Game Object, and return the information

@app.route('/getGameInfo', methods=['GET'])
def getGameInfo():
    gameDifficultyLevel = request.args.get('gameDifficultyLevel')
    userID = request.args.get('userID')

    currentPlayer = playerManager.getPlayer(playerID=userID)

    currentPlayer.updateInfo()

    createGameForPlayer(currentPlayer, gameDifficultyLevel)

    if currentPlayer.currentGame is not None:
        print(f"Created {gameDifficultyLevel} game for {currentPlayer.name}")
        arrayOfRoundDictionaries = currentPlayer.currentGame.startGame()
        return jsonify({"message": "Success", "description": f"Created {gameDifficultyLevel} game for {currentPlayer.name}", "roundsArray": arrayOfRoundDictionaries}), 200
    else:
        print(
            f"Could not create {gameDifficultyLevel} game for {currentPlayer.name}")
        return jsonify({"message": "No more games left"})


@app.route('/storeRoundGuesses', methods=['POST'])
def storeRoundGuess():

    if request.method == 'POST':

        # Get data from client

        data = request.json
        yearGuess: int = data.get('yearGuess')
        targetGuess: dict = data.get('targetGuess')

        targetGuess: list[float] = [targetGuess['x'], targetGuess['y']]
        userID: str = data.get('userID')

        # store their current round guesses

        try:

            currentPlayer: Player = playerManager.getPlayer(playerID=userID)

            currentPlayer.updateInfo()
            currentGame: Game = currentPlayer.currentGame

            currentGame.storeRound(yearGuess=yearGuess,
                                   targetGuess=targetGuess)

            # this is just for development purposes, we don't need this line
            currentRoundNumber = currentGame.currentRoundNumber - 1

            return jsonify({"message": "Success", "description": f"Stored guesses for Round #{currentRoundNumber} for player {currentPlayer.name}"})

        except Exception as e:

            error_message = str(e)
            return jsonify({"message": "Failed", "description": error_message})


# Gets the UID and scores the game, returning the score for each round and the total score.

@app.route('/endGame', methods=['GET'])
def endGameScoreAndReturnRounds():

    if request.method == 'GET':

        userID = request.args.get('userID')

        try:

            currentPlayer: Player = playerManager.getPlayer(playerID=userID)
            currentPlayer.updateInfo()
            currentGame: Game = currentPlayer.currentGame

            totalScore: int
            scoreForEachRound: list[int]
            placeOnTheLeaderboardString: str

            totalScore, scoreForEachRound = currentGame.endGame()

            return jsonify({"message": "Success", "totalScore": totalScore, "scoreForEachRound": scoreForEachRound})

        except Exception as e:
            error_message = str(e)
            return jsonify({"message": "Failed", "description": error_message})


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
    app.run(port=5000, host="0.0.0.0")


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

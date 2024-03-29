import sys

from UserModule.UserInterface import UserInterface
from GameModule.GameInterface import Game
from FirebaseAccess.firebase import db



players_ref = db.collection('players')

def get_players_data():
    docs = players_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict

class Player(UserInterface):
    def __init__(self, userID: str):
    
        self.userID = userID
        self.gameIDsPlayed : str = []
        self.name : str = ""
        self.email : str = ""
        self.currentGame : Game = None
        self.easyScore : int = 0
        self.mediumScore : int = 0
        self.hardScore : int = 0


    def signIn(self, email: str, password: str):
        # Implement sign-in logic here

        signInSuccessful : bool = True



        if signInSuccessful:

            # populate the name, email, score, gameIDsPlayed fields

            # Then, add the player object to the PlayerSessionManager array
            pass


        
    def updateInfo(self):

        playerDoc  = db.collection('players').document(self.userID).get()
        playerDictionary = playerDoc.to_dict()

        name = playerDictionary["name"]
        email = playerDictionary["email"]
        easyScore = playerDictionary["EasyScore"]
        mediumScore = playerDictionary["MediumScore"]
        hardScore = playerDictionary["HardScore"]
        gamesPlayed = playerDictionary["gamesPlayed"]

        self.name = name
        self.email = email
        self.easyScore = easyScore
        self.mediumScore = mediumScore
        self.hardScore = hardScore

        self.gameIDsPlayed = gamesPlayed

    def signOut(self):
        # Implement sign-out logic here
        pass

    def changeEmail(self, newEmail: str):
        self.email = newEmail

    def changePassword(self, newPassword: str):
        # Implement password change logic here
        pass

    def displayLeaderboard(self, difficulty: str):
        # Implement leaderboard display logic here, possibly filtering by difficulty
        pass
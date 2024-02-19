from UserInterface import UserInterface

from DifficultyModule.Difficulty import DifficultyEnum

import firebase_admin

from firebase_admin import credentials, firestore
cred = credentials.Certificate('jokerker-d9272-firebase-adminsdk-sbyd5-fda51193ba.json')
firebase_admin.initialize_app(cred)
db = firestore.client()


class Player(UserInterface):
    def __init__(self, userID: str):
    
        self.userID = userID

    def signIn(self, email: str, password: str):
        # Implement sign-in logic here

        signInSuccessful : bool = True



        if signInSuccessful:
            pass


        

    def signOut(self):
        # Implement sign-out logic here
        pass

    def changeEmail(self, newEmail: str):
        self.email = newEmail

    def changePassword(self, newPassword: str):
        # Implement password change logic here
        pass

    def displayLeaderboard(self, difficulty: DifficultyEnum):
        # Implement leaderboard display logic here, possibly filtering by difficulty
        pass
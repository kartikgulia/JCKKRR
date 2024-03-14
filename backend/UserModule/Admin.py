from FirebaseAccess.firebase import db

class Admin:
    def __init__(self):
        # Constructor method for Admin class
        self.easy_games_ref = db.collection('EasyGames')
        self.medium_games_ref = db.collection('MediumGames')
        self.hard_games_ref = db.collection('HardGames')

    def addGame(self, gameInfo: dict, difficulty: str):

        if difficulty.lower() == 'easy':
            self.easy_games_ref.add(gameInfo)
        elif difficulty.lower() == 'medium':
            self.medium_games_ref.add(gameInfo)
        elif difficulty.lower() == 'hard':
            self.hard_games_ref.add(gameInfo)
        else:
            print("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")

    def removeGame(self, gameID: str, difficulty: str):

        if difficulty.lower() == 'easy':
            self.easy_games_ref.document(gameID).delete()
        elif difficulty.lower() == 'medium':
            self.medium_games_ref.document(gameID).delete()
        elif difficulty.lower() == 'hard':
            self.hard_games_ref.document(gameID).delete()
        else:
            print("Invalid difficulty level. Please choose 'easy', 'medium', or 'hard'.")

import random
from abc import ABC, abstractmethod

from FirebaseAccess.firebase import db
from GameModule.Rounds import Round, BackgroundPicture


class Game(ABC):
    def __init__(self, player):
        
        self.player = player
        self.gameID = None
        self.rounds = []
        self.currentRoundNumber = 1
        self.gameID: str = None
        
        self.yearGuesses : list[int] = []
        self.targetGuesses : list[list[float]] = []



    def getArrayOfRoundDictionaries(self):
        arrayfRoundDicts = []
        for r in self.rounds:
            arrayfRoundDicts.append(r.getData())
        return arrayfRoundDicts
    

    def startGame(self):
        # Common starting game logic
        gamesCollectionRef = self.getGameCollectionRef()
        print("Game started with ID:", self.gameID)
        # Initialize or reset game state as needed
        self.currentRoundNumber = 1
        self.rounds = []
        # Populate rounds array with database info at self.gameID
        roundIDs = gamesCollectionRef.document(self.gameID).get().to_dict()
        roundCollectionRef = self.getRoundCollectionRef()
        # TODO: not sure how Kap will title it but I'm assuming its rounds. Change this later
        for ID in roundIDs["rounds"]:
            self.rounds.append(Round(ID, roundCollectionRef))
        arrayfRoundDicts = self.getArrayOfRoundDictionaries()
        return arrayfRoundDicts

    def setGameID(self):
        gamesCollectionRef = self.getGameCollectionRef()
        docs = gamesCollectionRef.get()

        gamesPlayed = set(self.player.gameIDsPlayed)
        gameIDsLeft = [doc.to_dict()['gameID'] for doc in docs if doc.to_dict()[
            'gameID'] not in gamesPlayed]

        if len(gameIDsLeft) == 0:
            return

        self.gameID = random.choice(gameIDsLeft)

    def storeRound(self, yearGuess, targetGuess):

        print(yearGuess)
        print(targetGuess)

        self.yearGuesses.append(yearGuess)
        self.targetGuesses.append(targetGuess)

        self.currentRoundNumber += 1



    @abstractmethod
    def getGameCollectionRef(self):
        pass

    @abstractmethod  # subject to change but I'm pretty sure we should have a ref to each round collection based on difficulty. 
                    # yeah thats good -- rayyan
    def getRoundCollectionRef(self):
        pass

    @abstractmethod
    def scoreRounds(self) -> tuple:
        pass


    def endGame(self) -> tuple:

        # Get scores and leaderboard position

        try:

            totalScore : int

            scoreForEachRound : list[int]

            totalScore, scoreForEachRound = self.scoreRounds()


            

            

            # End Game Logistics

            # 1) Add the current game id to the list of played games for the user

            self.player.gameIDsPlayed.append(self.gameID)

            
            # TODO : Update the Player document (document name: uid. in the 'players' collection)

            players_ref = db.collection('players')

            uid : str = self.player.userID

                # 2) TODO : Update their gameIDsPlayed with the self.player.gameIDsPlayed

        
                # 3) TODO : Update their total score in the database


            players_ref = db.collection('players')

            doc_ref = players_ref.document(uid)

            doc = doc_ref.get()

            doc_data : dict

            totalScoreInDatabase : int = 0

            if doc.exists:
                doc_data = doc.to_dict()
                print("Document data:", doc_data)


                prevScore = doc_data[f"{self.difficulty}Score"]

                totalScoreInDatabase = prevScore + totalScore

                doc_ref.update({
                    f"{self.difficulty}Score" : totalScoreInDatabase,
                    "gamesPlayed" : self.player.gameIDsPlayed
                })


            else:
                print("No such document!")


            # 4) Remove the game from player

            self.player.currentGame = None


            # 5) Update the leaderboard
            print(self.difficulty)
            leaderboard_ref = db.collection(f'{self.difficulty}Leaderboard')


            doc_ref = leaderboard_ref.document(uid)

            doc = doc_ref.get()

            doc_data : dict
            if doc.exists:
                doc_data = doc.to_dict()
                print("Document data:", doc_data)

                doc_ref.update({
                    f"Score" : totalScoreInDatabase,
                    "Name" : self.player.name,
                })


            else:
                print("No such document!")

                print("Creating document")

                doc_ref.set({
                    "Name" : self.player.name,
                    "Score" : totalScoreInDatabase,
                })
                


            return (totalScore, scoreForEachRound)
        

        except Exception as e:
            print(e)
            self.player.currentGame = None
            return (0,0)
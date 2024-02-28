from abc import ABC, abstractmethod
import random

class Game(ABC):
    def __init__(self, player):
        self.player = player
        self.gameID = None


    def startGame(self):
        # Common starting game logic
        gamesCollectionRef = self.getGameCollectionRef()
        print("Game started with ID:", self.gameID)
        # Initialize or reset game state as needed
        self.currentRoundNumber = 1
        self.rounds = []
        # Populate rounds array with database info at self.gameID
        
    def setGameID(self):
        gamesCollectionRef = self.getGameCollectionRef()
        docs = gamesCollectionRef.get()

        gamesPlayed = set(self.player.gameIDsPlayed)
        gameIDsLeft = [doc.to_dict()['gameID'] for doc in docs if doc.to_dict()['gameID'] not in gamesPlayed]

        if len(gameIDsLeft) == 0:
            return

        self.gameID = random.choice(gameIDsLeft)


    @abstractmethod
    def getGameCollectionRef(self):
        pass

    @abstractmethod
    def scoreRound(self):
        pass

    @abstractmethod
    def endGame(self):
        pass
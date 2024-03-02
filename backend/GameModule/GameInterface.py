import random
from abc import ABC, abstractmethod

from FirebaseAccess.firebase import db
from Rounds import BackgroundPicture, Round


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
        roundIDs = gamesCollectionRef.document(self.gameID).get()
        roundCollectionRef = self.getRoundCollectionRef()
        # not sure how Kap will title it but I'm assuming its rounds. Change this later
        for ID in roundIDs["rounds"]:
            self.rounds.append(Round(ID, roundCollectionRef))
        arrayfRoundDicts = []
        for r in self.rounds:
            arrayfRoundDicts.append(r.getData())
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

    @abstractmethod
    def getGameCollectionRef(self):
        pass

    @abstractmethod  # subject to change but I'm pretty sure we should have a ref to each round collection based on difficulty
    def getRoundCollectionRef(self):
        pass

    @abstractmethod
    def scoreRound(self):
        pass

    @abstractmethod
    def endGame(self):
        pass

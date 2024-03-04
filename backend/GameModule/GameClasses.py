import random
import sys
from enum import Enum

from FirebaseAccess.firebase import db
from GameModule.GameInterface import Game
from UserModule.Player import Player


class EasyGame(Game):
    def __init__(self, player):

        # Properties
        self.player: Player = player
        self.rounds = []
        self.currentRoundNumber = None
        self.gameID: str = None

    # Implementation of each function for EasyGame

    def getGameCollectionRef(self):
        easyGamesRef = db.collection("EasyGames")
        return easyGamesRef

    def getRoundCollectionRef(self):
        return db.collection("EasyRounds")

   

    def scoreRound(self):

        pass

    def endGame(self):

        pass


class MediumGame(Game):
    def __init__(self, player):
        self.player = player
        self.rounds = []

    def getGameCollectionRef(self):
        mediumGamesRef = db.collection("MediumGames")
        return mediumGamesRef

    def getRoundCollectionRef(self):
        return db.collection("MediumRounds")

 
    def scoreRound(self):

        pass

    def endGame(self):

        pass


class HardGame(Game):
    def __init__(self, player):
        self.player = player
        self.rounds = []

    def getGameCollectionRef(self):
        hardGamesRef = db.collection("HardGames")
        return hardGamesRef

    def getRoundCollectionRef(self):
        return db.collection("HardRounds")



    def scoreRound(self):

        pass

    def endGame(self):

        pass


# Factory class to create game objects
class GameFactory:
    def __init__(self, player):
        self.player = player

    def create_game(self, difficulty):
        if difficulty == "Easy":
            return EasyGame(self.player)
        elif difficulty == "Medium":
            return MediumGame(self.player)
        elif difficulty == "Hard":
            return HardGame(self.player)
        else:
            raise ValueError("Unknown difficulty level")

# Usage


if __name__ == "__main__":
    player = Player(userID="bo3bw4GUJdFhTp6aEqiD")  # Example player
    factory = GameFactory(player)
    easy_game = factory.create_game("Easy")
    easy_game.setGameID()
    print()

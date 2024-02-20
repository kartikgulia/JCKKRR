from GameModule.GameInterface import Game
from enum import Enum

import random


import sys




from UserModule.Player import Player

from FirebaseAccess.firebase import db

# Classes for different types of games
class EasyGame(Game):
    def __init__(self, player, rounds):
        

        easyGamesRef = db.collection("EasyGames")

        docs = easyGamesRef.get()


        # Properties
        self.player : Player = player
        self.rounds = rounds
        self.currentRoundNumber = 1
        
        self.easyGamesDict = {}
        for idx, doc in enumerate(docs, start=1):
            self.easyGamesDict[idx] = doc.to_dict()
        
        self.gameID : str = None



    

    # Implementation of each function for EasyGame
            

    def startGame(self):

        # This will start the Game progress
        pass


    def setGameID(self):

        # 3 steps will be performed in order to set the game ID. (This corresponds to the Game Select System Design I created)

        
        

        
        # 1) Get games played -- get the array of game ids the user played.

        # access player attribute's array of game ids played


        gamesPlayed = self.player.gameIDsPlayed
        gamesPlayedSet = set(gamesPlayed)
    
        

        # 2) Check if any games left -- for the selected difficulty, go through the corresponding "Games" collection and check if there's at least 1 game left. Return array of games left.

        gameIDsLeft : list[str] = []


        for num, gameDoc in self.easyGamesDict.items():

            gameID = gameDoc['gameID']

            if gameID not in gamesPlayedSet:

                gameIDsLeft.append(gameID)


        if len(gameIDsLeft) == 0:
            return 


        # 3) Randomly return a game from the array of games left.

        random_index = random.randint(0, len(gameIDsLeft)-1)

        randomGameID : str = gameIDsLeft[random_index]

        self.gameID = randomGameID


    def playRounds(self):

        pass

    def playRound(self):

        pass

    def endGame(self):

        pass

class MediumGame(Game):
    def __init__(self, player, rounds):
        self.player = player
        self.rounds = rounds

    # The methods would have their own implementations similar to EasyGame
    # ...

class HardGame(Game):
    def __init__(self, player, rounds):
        self.player = player
        self.rounds = rounds

    # The methods would have their own implementations similar to EasyGame
    # ...

# Factory class to create game objects
class GameFactory:
    def __init__(self, player):
        self.player = player

    def create_game(self, difficulty):
        if difficulty == "Easy":
            return EasyGame(self.player, [])
        elif difficulty == "Medium":
            return MediumGame(self.player, [])
        elif difficulty == "Hard":
            return HardGame(self.player, [])
        else:
            raise ValueError("Unknown difficulty level")

# Usage
        
if __name__ == "__main__":
    player = Player(userID="bo3bw4GUJdFhTp6aEqiD")  # Example player
    factory = GameFactory(player)
    easy_game = factory.create_game("Easy")
    easy_game.setGameID()
    print()
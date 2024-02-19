from GameInterface import Game
from enum import Enum
from app import db


# Enum for Difficulty Levels
class Difficulty(Enum):
    EASY = "Easy"
    NORMAL = "Medium"
    HARD = "Hard"

# Classes for different types of games
class EasyGame(Game):
    def __init__(self, player, rounds):
        self.player = player
        self.rounds = rounds
    

    # Implementation of each function for EasyGame
    def startGame(self):

        pass

    def getGameID(self):

        # 3 steps will be performed in order to get the game ID. (This corresponds to the Game Select System Design I created)

        
        game_ref = db.collection("EasyGames")

        
        # 1) Get games played -- get the array of game ids the user played. Get games of the Easy difficulty

        player_ref = db.collection("players")

        docs = game_ref.get()

        
        

        # 2) Check if any games left -- for the selected difficulty, go through the corresponding "Games" collection and check if there's at least 1 game left. Return array of games left.

        # 3) Randomly return a game from the array of games left.

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
        if difficulty == Difficulty.EASY:
            return EasyGame(self.player, [])
        elif difficulty == Difficulty.NORMAL:
            return MediumGame(self.player, [])
        elif difficulty == Difficulty.HARD:
            return HardGame(self.player, [])
        else:
            raise ValueError("Unknown difficulty level")

# Usage
player = "John Doe"  # Example player, could be an instance of a User class
factory = GameFactory(player)
easy_game = factory.create_game(Difficulty.EASY)

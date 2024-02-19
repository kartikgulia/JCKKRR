from abc import ABC, abstractmethod
from enum import Enum

# Interface for the game
class Game(ABC):
    @abstractmethod
    def startGame(self):
        pass

    @abstractmethod
    def getRounds(self):
        pass

    @abstractmethod
    def playRounds(self):
        pass

    @abstractmethod
    def playRound(self):
        pass

    @abstractmethod
    def endGame(self):
        pass

# Enum for Difficulty Levels
class Difficulty(Enum):
    EASY = 1
    NORMAL = 2
    HARD = 3

# Classes for different types of games
class EasyGame(Game):
    def __init__(self, player, rounds):
        self.player = player
        self.rounds = rounds
    

    # Implementation of each function for EasyGame
    def startGame(self):

        pass

    def getRounds(self):

        pass

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

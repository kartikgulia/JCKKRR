from abc import ABC, abstractmethod


# Interface for the game
class Game(ABC):
    @abstractmethod
    def startGame(self):
        pass

    @abstractmethod
    def setGameID(self):
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
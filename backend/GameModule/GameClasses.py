import random
import sys
from enum import Enum
import math


from GameModule.GameInterface import Game
from UserModule.Player import Player
from GameModule.Rounds import Round
from FirebaseAccess.firebase import db

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

   

    def scoreRounds(self) -> int:

        yearGuesses = [1970, 1940, 1955]
        locationGuesses = [[300,500], [400,500], [500,500]]
        
        currentRoundNumber : int = 0

        totalScore : int = 0
        
        for round in self.rounds:
        
            round : Round = round

            # 1) Get the actual answers
            currentData : dict = round.getData()
            correctYear : int = currentData["yearTaken"]
            correctLocation : list[list[int]] = currentData["targetImageCoordinates"]    

            # 2) Manipulate correctLocation data to get the average "pinpoint"

            bottomLeftCoord : list[int] = correctLocation[0]
            topRightCoord : list[int] = correctLocation[2]
        
            correctCoord : list[int] = [abs(topRightCoord[0]-bottomLeftCoord[0]), abs(topRightCoord[1]-bottomLeftCoord[1])]

            # 3) Compare the correct vs. guesses

            # Max score for each is 2024 (50-50 split)
            
            yearScore : int = 2024 - abs(correctYear-yearGuesses[currentRoundNumber])

            locationDifference = math.sqrt(math.pow(correctCoord[0]-locationGuesses[currentRoundNumber][0],2) + math.pow(correctCoord[1]-locationGuesses[currentRoundNumber][1], 2))

            locationScore : int
            
            if locationDifference > 2024:
                locationScore = 0
            else:
                locationScore = 2024 - locationDifference

            if locationScore < 1974:
                locationScore += 50

            if yearScore < 1974:
                yearScore += 50

            totalScore += yearScore
            totalScore += locationScore

            currentRoundNumber += 1

        return totalScore  

    def endGame(self):

        pass


class MediumGame(Game):
    def __init__(self, player):
        self.player: Player = player
        self.rounds = []
        self.currentRoundNumber = None
        self.gameID: str = None

    def getGameCollectionRef(self):
        mediumGamesRef = db.collection("MediumGames")
        return mediumGamesRef

    def getRoundCollectionRef(self):
        return db.collection("MediumRounds")

 
    def scoreRounds(self) -> int:

        yearGuesses = [1970, 1940, 1955]
        locationGuesses = [[300,500], [400,500], [500,500]]
        
        currentRoundNumber : int = 0

        totalScore : int = 0
        
        for round in self.rounds:
        
            round : Round = round

            # 1) Get the actual answers
            currentData : dict = round.getData()
            correctYear : int = currentData["yearTaken"]
            correctLocation : list[list[int]] = currentData["targetImageCoordinates"]    

            # 2) Manipulate correctLocation data to get the average "pinpoint"

            bottomLeftCoord : list[int] = correctLocation[0]
            topRightCoord : list[int] = correctLocation[2]
        
            correctCoord : list[int] = [abs(topRightCoord[0]-bottomLeftCoord[0]), abs(topRightCoord[1]-bottomLeftCoord[1])]

            # 3) Compare the correct vs. guesses

            # Max score for each is 2024 (50-50 split)
            
            yearScore : int = 2024 - abs(correctYear-yearGuesses[currentRoundNumber])

            locationDifference = math.sqrt(math.pow(correctCoord[0]-locationGuesses[currentRoundNumber][0],2) + math.pow(correctCoord[1]-locationGuesses[currentRoundNumber][1], 2))

            locationScore : int
            
            if locationDifference > 2024:
                locationScore = 0
            else:
                locationScore = 2024 - locationDifference

            if locationScore < 1999:
                locationScore += 25

            if yearScore < 1999:
                yearScore += 25

            totalScore += yearScore
            totalScore += locationScore

            currentRoundNumber += 1

        return totalScore  

    def endGame(self):

        pass


class HardGame(Game):
    def __init__(self, player):
        self.player: Player = player
        self.rounds = []
        self.currentRoundNumber = None
        self.gameID: str = None

    def getGameCollectionRef(self):
        hardGamesRef = db.collection("HardGames")
        return hardGamesRef

    def getRoundCollectionRef(self):
        return db.collection("HardRounds")


    def scoreRounds(self, yearGuesses, locationGuesses) -> int:

        yearGuesses = [1970, 1940, 1955]
        locationGuesses = [[300,500], [400,500], [500,500]]
        
        currentRoundNumber : int = 0

        totalScore : int = 0
        
        for round in self.rounds:
        
            round : Round = round

            # 1) Get the actual answers
            currentData : dict = round.getData()
            correctYear : int = currentData["yearTaken"]
            correctLocation : list[list[int]] = currentData["targetImageCoordinates"]    

            # 2) Manipulate correctLocation data to get the average "pinpoint"

            bottomLeftCoord : list[int] = correctLocation[0]
            topRightCoord : list[int] = correctLocation[2]
        
            correctCoord : list[int] = [abs(topRightCoord[0]-bottomLeftCoord[0]), abs(topRightCoord[1]-bottomLeftCoord[1])]

            # 3) Compare the correct vs. guesses

            # Max score for each is 2024 (50-50 split)
            
            yearScore : int = 2024 - abs(correctYear-yearGuesses[currentRoundNumber])

            locationDifference = math.sqrt(math.pow(correctCoord[0]-locationGuesses[currentRoundNumber][0],2) + math.pow(correctCoord[1]-locationGuesses[currentRoundNumber][1], 2))

            locationScore : int
            
            if locationDifference > 2024:
                locationScore = 0
            else:
                locationScore = 2024 - locationDifference

            totalScore += yearScore
            totalScore += locationScore

            currentRoundNumber += 1

        return totalScore            

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

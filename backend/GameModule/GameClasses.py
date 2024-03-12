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
        super().__init__(player)
        # Properties
        self.player: Player = player
        
        self.difficulty = "Easy"
    # Implementation of each function for EasyGame

    def getGameCollectionRef(self):
        easyGamesRef = db.collection("EasyGames")
        return easyGamesRef

    def getRoundCollectionRef(self):
        return db.collection("EasyRounds")

   

    def scoreRounds(self) -> int:

        yearGuesses = self.yearGuesses
        locationGuesses = self.targetGuesses
        scoreForEachRound = []

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

            correctCoord : list[int] = [0,0]

            if(bottomLeftCoord[0] == 0):
                correctCoord[0] = topRightCoord[0]/2
            else: 
                correctCoord[0] = abs(topRightCoord[0]-bottomLeftCoord[0])
            if(bottomLeftCoord[1] == 0):
                correctCoord[1] = topRightCoord[1]/2
            else:  
                correctCoord[1] = abs(topRightCoord[1]-bottomLeftCoord[1])
     
                # correctCoord : list[int] = [abs(topRightCoord[0]-bottomLeftCoord[0]), abs(topRightCoord[1]-bottomLeftCoord[1])]

            # 3) Compare the correct vs. guesses

            # Max score for each is 2024 (50-50 split)
            correctYear = int(correctYear)
            yearScore : int = 2024 - abs(correctYear-yearGuesses[currentRoundNumber])

            locationDifference = math.sqrt(math.pow(correctCoord[0]-locationGuesses[currentRoundNumber][0],2) + math.pow(correctCoord[1]-locationGuesses[currentRoundNumber][1], 2))

            locationScore : int
            
            if locationDifference > 2024:
                locationScore = 0
            else:
                locationScore = 2024 - locationDifference

            if locationScore < 1974:
                locationScore += 50
            elif locationScore >= 1974:
                locationScore = 2024

            if yearScore < 1974:
                yearScore += 50
            elif yearScore >= 1974: 
                yearScore = 2024

            eachRoundScore = int(yearScore + locationScore)
            scoreForEachRound.append(eachRoundScore)
            totalScore +=  eachRoundScore

            currentRoundNumber += 1

        return totalScore, scoreForEachRound  
    


class MediumGame(Game):
    def __init__(self, player):
        super().__init__(player)
        self.player: Player = player
        self.difficulty = "Medium"
    def getGameCollectionRef(self):
        mediumGamesRef = db.collection("MediumGames")
        return mediumGamesRef

    def getRoundCollectionRef(self):
        return db.collection("MediumRounds")

 
    def scoreRounds(self) -> int:

        yearGuesses = self.yearGuesses
        locationGuesses = self.targetGuesses
        scoreForEachRound = []

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
        
            correctCoord : list[int] = [0,0]

            if(bottomLeftCoord[0] == 0):
                correctCoord[0] = topRightCoord[0]/2
            else: 
                correctCoord[0] = abs(topRightCoord[0]-bottomLeftCoord[0])
            if(bottomLeftCoord[1] == 0):
                correctCoord[1] = topRightCoord[1]/2
            else:  
                correctCoord[1] = abs(topRightCoord[1]-bottomLeftCoord[1])

            #correctCoord : list[int] = [abs(topRightCoord[0]-bottomLeftCoord[0]), abs(topRightCoord[1]-bottomLeftCoord[1])]

            # 3) Compare the correct vs. guesses

            # Max score for each is 2024 (50-50 split)
            correctYear = int(correctYear)
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

            eachRoundScore = int(yearScore + locationScore)
            scoreForEachRound.append(eachRoundScore)
            totalScore +=  eachRoundScore

            currentRoundNumber += 1

        return totalScore, scoreForEachRound  




class HardGame(Game):
    def __init__(self, player):
        super().__init__(player)
        self.player: Player = player
        self.difficulty = "Hard"

    def getGameCollectionRef(self):
        hardGamesRef = db.collection("HardGames")
        return hardGamesRef

    def getRoundCollectionRef(self):
        return db.collection("HardRounds")


    def scoreRounds(self) -> int:

        scoreForEachRound = []

        yearGuesses = self.yearGuesses
        locationGuesses = self.targetGuesses
        
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
            correctYear = int(correctYear)
            yearScore : int = 2024 - abs(correctYear-yearGuesses[currentRoundNumber])

            locationDifference = math.sqrt(math.pow(correctCoord[0]-locationGuesses[currentRoundNumber][0],2) + math.pow(correctCoord[1]-locationGuesses[currentRoundNumber][1], 2))

            locationScore : int
            
            if locationDifference > 2024:
                locationScore = 0
            else:
                locationScore = 2024 - locationDifference

            eachRoundScore = int(yearScore + locationScore)
            scoreForEachRound.append(eachRoundScore)
            totalScore +=  eachRoundScore

            currentRoundNumber += 1

        return totalScore, scoreForEachRound            



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

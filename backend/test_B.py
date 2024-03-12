# test_easy_game.py

import pytest
from GameModule.GameClasses import EasyGame  # Updated import statement
from UserModule.Player import Player
from FirebaseAccess.firebase import db

# Test for EasyGame class
class TestEasyGame:
    # Test initialization of EasyGame class
    def test_init(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        easy_game = EasyGame(mock_player)
        assert easy_game.player == mock_player
        assert easy_game.difficulty == "Easy"

    # Test getGameCollectionRef method
    def test_get_game_collection_ref(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        easy_game = EasyGame(mock_player)
        collection_ref = easy_game.getGameCollectionRef()
        assert collection_ref == db.collection("EasyGames")

    # Test getRoundCollectionRef method
    def test_get_round_collection_ref(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        easy_game = EasyGame(mock_player)
        collection_ref = easy_game.getRoundCollectionRef()
        assert collection_ref == db.collection("EasyRounds")

    # Test scoreRounds method for easy game WITHOUT rounding (1 round)
    def test_score_easyrounds_worounding(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        easy_game = EasyGame(mock_player)
        easy_game.yearGuesses = [2010, 2000] # second in list should account for easy rounding
        easy_game.targetGuesses = [[5,5], [10,10]] # second in list should account for easy rounding
        # Mocking Round data
        class MockRound1:
            def getData(self):
                return {"yearTaken": 2010, "targetImageCoordinates": [[0, 0], [0, 10], [10, 10], [10, 0]]}
        class MockRound2:
            def getData(self):
                return {"yearTaken": 2000, "targetImageCoordinates": [[0, 0], [0, 20], [20, 20], [20, 0]]}
        easy_game.rounds = [MockRound1(), MockRound2()]
        total_score = easy_game.scoreRounds()
        assert total_score[0] == 8096  # Total score for both rounds
        assert total_score[1] == [4048,4048]  # Score for each round

    # Test scoreRounds method for easy game WITH rounding (1 round)
    def test_score_easyrounds_wrounding(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        easy_game = EasyGame(mock_player)
        easy_game.yearGuesses = [1961, 2040] # second in list should account for easy rounding
        easy_game.targetGuesses = [[40,40], [45,45]] # second in list should account for easy rounding
        # Mocking Round data
        class MockRound1:
            def getData(self):
                return {"yearTaken": 2010, "targetImageCoordinates": [[0, 0], [0, 10], [10, 10], [10, 0]]}
        class MockRound2:
            def getData(self):
                return {"yearTaken": 2000, "targetImageCoordinates": [[0, 0], [0, 20], [20, 20], [20, 0]]}
        easy_game.rounds = [MockRound1(), MockRound2()]
        total_score = easy_game.scoreRounds()
        assert total_score[0] == 8096  # Total score for both rounds
        assert total_score[1] == [4048,4048]  # Score for each round

    # Add more test cases for other scenarios and edge cases as needed

if __name__ == "__main__":
    pytest.main()

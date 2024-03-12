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

    # Test scoreRounds method
    def test_score_rounds(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        easy_game = EasyGame(mock_player)
        easy_game.yearGuesses = [2000, 2020]
        easy_game.targetGuesses = [[5,5], [200, 250]]
        # Mocking Round data
        class MockRound:
            def getData(self):
                return {"yearTaken": 2010, "targetImageCoordinates": [[0, 0], [0, 10], [10, 10], [10, 0]]}
        easy_game.rounds = [MockRound(), MockRound()]
        total_score, score_for_each_round = easy_game.scoreRounds()
        assert total_score == 4048  # Total score for both rounds
        assert score_for_each_round == [2024, 2024]  # Score for each round

    # Add more test cases for other scenarios and edge cases as needed

if __name__ == "__main__":
    pytest.main()

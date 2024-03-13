# test_easy_game.py

import pytest
from GameModule.GameClasses import *  # Updated import statement
from GameModule.gameCreationFunctions import *  # Updated import statement
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

    # Test scoreRounds method for easy game WITHOUT rounding (2 round)
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

    # Test scoreRounds method for easy game WITH rounding (2 round)
    def test_score_easyrounds_wrounding(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        easy_game = EasyGame(mock_player)
        easy_game.yearGuesses = [1961, 2051] # second in list should account for easy rounding
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
        assert total_score[0] == 8095  # Total score for both rounds
        assert total_score[1] == [4048,4047]  # Score for each round

    # Test scoreRounds method for easy game edge cases (1 round)
    def test_score_easyrounds_edgecases(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        easy_game = EasyGame(mock_player)
        easy_game.yearGuesses = [2000] # second in list should account for easy rounding
        easy_game.targetGuesses = [[10000,10000]] # second in list should account for easy rounding
        # Mocking Round data
        class MockRound1:
            def getData(self):
                return {"yearTaken": 2000, "targetImageCoordinates": [[10, 10], [10, 25], [25, 25], [25, 10]]}
        easy_game.rounds = [MockRound1()]
        total_score = easy_game.scoreRounds()
        assert total_score[0] == 2074  # Total score for both rounds
        assert total_score[1] == [2074]  # Score for each round    

    # Add more test cases for other scenarios and edge cases as needed



class TestMediumGame:
    # Test initialization of MediumGame class
    def test_init(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        medium_game = MediumGame(mock_player)
        assert medium_game.player == mock_player
        assert medium_game.difficulty == "Medium"

    # Test getGameCollectionRef method
    def test_get_game_collection_ref(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        medium_game = MediumGame(mock_player)
        collection_ref = medium_game.getGameCollectionRef()
        assert collection_ref == db.collection("MediumGames")

    # Test getRoundCollectionRef method
    def test_get_round_collection_ref(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        medium_game = MediumGame(mock_player)
        collection_ref = medium_game.getRoundCollectionRef()
        assert collection_ref == db.collection("MediumRounds")

    # Test scoreRounds method for medium game without rounding
    def test_score_mediumrounds_worounding(self): 
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        medium_game = MediumGame(mock_player)
        medium_game.yearGuesses = [2010, 2000]
        medium_game.targetGuesses = [[5, 5], [10, 10]]
        # Mocking Round data
        class MockRound1:
            def getData(self):
                return {"yearTaken": 2010, "targetImageCoordinates": [[0, 0], [0, 10], [10, 10], [10, 0]]}
        class MockRound2:
            def getData(self):
                return {"yearTaken": 2000, "targetImageCoordinates": [[0, 0], [0, 20], [20, 20], [20, 0]]}
        medium_game.rounds = [MockRound1(), MockRound2()]
        total_score, score_for_each_round = medium_game.scoreRounds()
        assert total_score == 8096  # Total score for both rounds
        assert score_for_each_round == [4048, 4048]  # Score for each round

    # Test scoreRounds method for medium game with rounding
    def test_score_mediumrounds_wrounding(self): #with rounding
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        medium_game = MediumGame(mock_player)
        medium_game.yearGuesses = [1992, 2026]
        medium_game.targetGuesses = [[5, 5], [10, 10]]
        # Mocking Round data
        class MockRound1:
            def getData(self):
                return {"yearTaken": 2010, "targetImageCoordinates": [[0, 0], [0, 10], [10, 10], [10, 0]]}
        class MockRound2:
            def getData(self):
                return {"yearTaken": 2000, "targetImageCoordinates": [[0, 0], [0, 20], [20, 20], [20, 0]]}
        medium_game.rounds = [MockRound1(), MockRound2()]
        total_score, score_for_each_round = medium_game.scoreRounds()
        assert total_score == 8095  # Total score for both rounds
        assert score_for_each_round == [4048, 4047]  # Score for each round

    # Test scoreRounds method for medium game edge cases
    def test_score_mediumrounds_edgecases(self): #with rounding
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        medium_game = MediumGame(mock_player)
        medium_game.yearGuesses = [1000]
        medium_game.targetGuesses = [[10000,1000]]
        # Mocking Round data
        class MockRound1:
            def getData(self):
                return {"yearTaken": 2000, "targetImageCoordinates": [[10, 10], [10, 25], [25, 25], [25, 10]]}
        medium_game.rounds = [MockRound1()]
        total_score, score_for_each_round = medium_game.scoreRounds()
        assert total_score == 1074  # Total score for both rounds
        assert score_for_each_round == [1074]  # Score for each round

    # Add more test cases for other scenarios and edge cases as needed
        


# Test for HardGame class
class TestHardGame:
    # Test initialization of HardGame class
    def test_init(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        hard_game = HardGame(mock_player)
        assert hard_game.player == mock_player
        assert hard_game.difficulty == "Hard"

    # Test getGameCollectionRef method
    def test_get_game_collection_ref(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        hard_game = HardGame(mock_player)
        collection_ref = hard_game.getGameCollectionRef()
        assert collection_ref == db.collection("HardGames")

    # Test getRoundCollectionRef method
    def test_get_round_collection_ref(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        hard_game = HardGame(mock_player)
        collection_ref = hard_game.getRoundCollectionRef()
        assert collection_ref == db.collection("HardRounds")

    # Test scoreRounds method for hard game without rounding
    def test_score_hardrounds_worounding(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        hard_game = HardGame(mock_player)
        hard_game.yearGuesses = [2000, 2011]
        hard_game.targetGuesses = [[5, 5], [10, 10]]
        # Mocking Round data
        class MockRound1:
            def getData(self):
                return {"yearTaken": 2000, "targetImageCoordinates": [[0, 0], [0, 10], [10, 10], [10, 0]]}
        class MockRound2:
            def getData(self):
                return {"yearTaken": 2010, "targetImageCoordinates": [[0, 0], [0, 20], [20, 20], [20, 0]]}
        hard_game.rounds = [MockRound1(), MockRound2()]
        total_score, score_for_each_round = hard_game.scoreRounds()
        assert total_score == 8095  # Total score for both rounds
        assert score_for_each_round == [4048, 4047]  # Score for each round

    # Test scoreRounds method for hard game edge cases
    def test_score_hardrounds_edgecases(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        hard_game = HardGame(mock_player)
        hard_game.yearGuesses = [1000]
        hard_game.targetGuesses = [[10000,10000]]
        # Mocking Round data
        class MockRound1:
            def getData(self):
                return {"yearTaken": 2000, "targetImageCoordinates": [[10, 10], [10, 25], [25, 25], [25, 10]]}
        hard_game.rounds = [MockRound1()]
        total_score, score_for_each_round = hard_game.scoreRounds()
        assert total_score == 1024  # Total score for both rounds
        assert score_for_each_round == [1024]  # Score for each round
    # Add more test cases for other scenarios and edge cases as needed
        


# Test for GameFactory class
class TestGameFactory:
    # Test initialization of GameFactory class
    def test_init(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game_factory = GameFactory(mock_player)
        assert game_factory.player == mock_player

    # Test create_game method for Easy difficulty
    def test_create_game_easy(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game_factory = GameFactory(mock_player)
        game = game_factory.create_game("Easy")
        assert isinstance(game, EasyGame)
        assert game.difficulty == "Easy"
        assert game.player == mock_player

    # Test create_game method for Medium difficulty
    def test_create_game_medium(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game_factory = GameFactory(mock_player)
        game = game_factory.create_game("Medium")
        assert isinstance(game, MediumGame)
        assert game.difficulty == "Medium"
        assert game.player == mock_player

    # Test create_game method for Hard difficulty
    def test_create_game_hard(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game_factory = GameFactory(mock_player)
        game = game_factory.create_game("Hard")
        assert isinstance(game, HardGame)
        assert game.difficulty == "Hard"
        assert game.player == mock_player

    # Test create_game method for invalid difficulty
    def test_create_game_invalid_difficulty(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game_factory = GameFactory(mock_player)
        with pytest.raises(ValueError):
            game_factory.create_game("InvalidDifficulty")


# Test for createGameForPlayer function
class TestCreateGameForPlayer:
    # Test creating game for player with valid parameters
    def test_create_game_for_player_valid(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game_difficulty = "Easy"
        # factory = GameFactory(mock_player)
        createGameForPlayer(mock_player, game_difficulty)
        assert mock_player.currentGame is not None
        assert isinstance(mock_player.currentGame, Game)
        assert mock_player.currentGame.difficulty == game_difficulty

    # Test creating game for player with invalid difficulty
    def test_create_game_for_player_invalid_difficulty(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game_difficulty = "InvalidDifficulty"
        # factory = GameFactory(mock_player)
        with pytest.raises(ValueError):
            createGameForPlayer(mock_player, game_difficulty)
        assert mock_player.currentGame is None

    # Test creating game for player when gameID is None
    def test_create_game_for_player_none_gameID(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game_difficulty = "Easy"
        factory = GameFactory(mock_player)
        createGameForPlayer(mock_player, game_difficulty)
        assert mock_player.currentGame is not None
        assert mock_player.currentGame.gameID is None


if __name__ == "__main__":
    pytest.main()

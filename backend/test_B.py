# test_easy_game.py

import pytest
from GameModule.GameClasses import *  # Updated import statement
from GameModule.gameCreationFunctions import *  # Updated import statement
from GameModule.Rounds import *  # Updated import statement
from UserModule.Player import Player
from unittest.mock import MagicMock
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

    # # Test creating game for player when gameID is None
    # def test_create_game_for_player_none_gameID(self):
    #     mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
    #     game_difficulty = "Easy"
    #     factory = GameFactory(mock_player)
    #     createGameForPlayer(mock_player, game_difficulty)
    #     assert mock_player.currentGame is not None
    #     assert mock_player.currentGame.gameID is None


class TestGame:
    def test_get_array_of_round_dictionaries(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game = EasyGame(mock_player)
        
        # Mocking a Round object and appending it to the rounds list
        class MockRound:
            def getData(self):
                return {"key": "value"}  # Example data
                
        mock_round = MockRound()
        game.rounds.append(mock_round)
        
        # Call the method to be tested
        result = game.getArrayOfRoundDictionaries()
        
        # Assertion
        assert len(result) == 1  # Check if there is one dictionary in the result
        assert result[0] == {"key": "value"}  # Check if the dictionary is as expected

    def test_storeRound(self):
        # Mock player and game
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game = EasyGame(mock_player)
        
        # Mock input values
        year_guess = "2000"
        target_guess = [10, 10]

        # Call the method to be tested
        game.storeRound(year_guess, target_guess)

        # Assertions
        assert year_guess in game.yearGuesses  # Check if year guess is stored
        assert target_guess in game.targetGuesses  # Check if target guess is stored
        assert game.currentRoundNumber == 2  # Check if current round number is updated

    def test_startGame(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game = EasyGame(mock_player)
        
        # Mocking gameID and rounds data
        game.gameID = "test_game_id"
        round_data = {"rounds": ["round1_id", "round2_id"]}  # Example round data
        
        # Mocking the database calls
        games_collection_ref_mock = MagicMock()
        games_collection_ref_mock.document().get().to_dict.return_value = round_data
        round_collection_ref_mock = MagicMock()
        
        # Assigning the mocks to the game object
        game.getGameCollectionRef = MagicMock(return_value=games_collection_ref_mock)
        game.getRoundCollectionRef = MagicMock(return_value=round_collection_ref_mock)
        
        # Testing the method
        game.startGame()
        
        # Asserting the result
        assert len(game.rounds) == 2  # Ensure that two rounds are appended to the rounds list


    def test_endGame(self):
        mock_player = Player("mRafsYCe9zWbCFNIcIIZhJoHSFn2")
        game = EasyGame(mock_player)
        game.gameID = "test_game_id"
        game.player.gameIDsPlayed = []
        game.difficulty = "Easy"
        game.scoreRounds = MagicMock(return_value=(100, [50, 50]))
        game.getGameCollectionRef = MagicMock()
        game.getRoundCollectionRef = MagicMock()

        # Call the method to be tested
        result = game.endGame()

        # Assertions
        assert result == (100, [50, 50])  # Check the return value
        assert game.player.gameIDsPlayed == ["test_game_id"]  # Check if game ID is added to player's game IDs
        assert game.player.currentGame is None  # Check if the current game is set to None

    def test_endGame_exception_handling(self):
        # Mocking player
        mock_player = MagicMock()
        mock_player.userID = "mRafsYCe9zWbCFNIcIIZhJoHSFn2"
        mock_player.gameIDsPlayed = []
        mock_player.name = "Test Player"

        # Mocking game
        game = EasyGame(mock_player)
        game.gameID = "test_game_id"
        game.difficulty = "Easy"
        game.scoreRounds = MagicMock(side_effect=Exception("Error occurred"))
        game.getGameCollectionRef = MagicMock()
        game.getRoundCollectionRef = MagicMock()

        # Call the method to be tested
        result = game.endGame()

        # Assertions
        assert result == (0, 0)  # Check the return value in case of exception
        assert game.player.currentGame is None  # Check if the current game is set to None

class TestRounds:
    def test_init_with_data(self):
        # Mock document with data
        mock_document = MagicMock()
        mock_document.to_dict.return_value = {
            'url': 'mock_url',
            'date': 2000,
            'BL': [1, 1],
            'TL': [1, 2],
            'TR': [2, 2],
            'BR': [2, 1]
        }

        # Create BackgroundPicture instance
        bg_picture = BackgroundPicture(mock_document)

        # Assertions
        assert bg_picture.filepath == 'mock_url'
        assert bg_picture.targetDate == 2000
        assert bg_picture.targetImageCoordinates == [[1, 1], [1, 2], [2, 2], [2, 1]]

    def test_init_without_data(self):
        # Mock document without data
        mock_document = MagicMock()
        mock_document.to_dict.return_value = None

        # Create BackgroundPicture instance
        bg_picture = BackgroundPicture(mock_document)

        # Assertions
        assert bg_picture.filepath == "https://live.staticflickr.com/65535/53483308986_eeb182d542.jpg"
        assert bg_picture.targetDate == 1989
        assert bg_picture.targetImageCoordinates == [[1, 2], [1, 4], [4, 4], [4, 2]]

if __name__ == "__main__":
    pytest.main()

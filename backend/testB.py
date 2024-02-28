# test_easy_games.py

import unittest
from unittest.mock import MagicMock
from app import *

class TestGetEasyGamesRefData(unittest.TestCase):
    def setUp(self):
        # Mocking EasyGames_ref
        self.mock_easy_games_ref = MagicMock()
        self.mock_document1 = MagicMock()
        self.mock_document1.to_dict.return_value = {'name': 'Game 1', 'difficulty': 'easy'}
        self.mock_document2 = MagicMock()
        self.mock_document2.to_dict.return_value = {'name': 'Game 2', 'difficulty': 'easy'}
        self.mock_easy_games_ref.get.return_value = [self.mock_document1, self.mock_document2]

    def test_get_easy_games_ref_data(self):
        # Call the function with the mocked EasyGames_ref
        easy_games_data = get_EasyGames_ref_data(self.mock_easy_games_ref)

        # Assertions to check if the function returns the expected data
        self.assertEqual(len(easy_games_data), 2)
        self.assertEqual(easy_games_data[1], {'name': 'Game 1', 'difficulty': 'easy'})
        self.assertEqual(easy_games_data[2], {'name': 'Game 2', 'difficulty': 'easy'})

if __name__ == '__main__':
    unittest.main()

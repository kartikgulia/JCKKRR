from GameModule.GameInterface import Game
from GameModule.GameClasses import GameFactory
from UserModule.Player import Player
from GameModule.Rounds import Round
from FirebaseAccess.firebase import db


player = Player(userID="bo3bw4GUJdFhTp6aEqiD")  # Example player
factory = GameFactory(player)
easy_game = factory.create_game("Easy")
easy_game.setGameID()

# Should populate self.rounds
easy_game.startGame()
# user will do frontend guesses

# user presses enter and sends back data for this
score = easy_game.scoreRounds()

print()
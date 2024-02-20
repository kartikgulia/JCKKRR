from GameModule.GameClasses import GameFactory
from UserModule.Player import Player

def createGameForPlayer(player : Player, gameDifficulty : str):

    factory = GameFactory(player)
    game = factory.create_game(gameDifficulty)

    player.currentGame = game
    
    return ""
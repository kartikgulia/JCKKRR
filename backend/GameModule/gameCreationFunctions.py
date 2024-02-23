from GameModule.GameClasses import GameFactory, Game
from UserModule.Player import Player

def createGameForPlayer(player : Player, gameDifficulty : str):

    factory = GameFactory(player)
    game : Game = factory.create_game(gameDifficulty)

    
    game.setGameID()

    if game.gameID == None:
        return
    
    player.currentGame = game
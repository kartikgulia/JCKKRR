from UserModule.Player import Player


# This file is to store players that have recently been on the website.

# We do this by creating a player ID : Player object mapping where played ID

# This ensures that:

#   1) We can keep track of their status (in the middle of a game, logged in already)
#   2) We don't have to create new objects every time a player accesses the database.



class PlayerSessionManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PlayerSessionManager, cls).__new__(cls)
            # Initialize any variables that need to be in the singleton here
            cls._instance.activePlayerSessions = {}
        return cls._instance

    def addPlayer(self, playerID: str, playerObject: Player):
        self.activePlayerSessions[playerID] = playerObject

    def getPlayer(self, playerID: str) -> Player:
        return self.activePlayerSessions.get(playerID, None)
    

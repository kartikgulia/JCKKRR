class BackgroundImage:
    def _init_(self):
        self.targetImage = ""
        self.filepath = ""  # get from database
        self.targetDate = ""
        self.imageCoordinates = []  # TL, TR, BL, BR

    # def getTargetImage(self, pixelCoords, filepath): # get target image either from database or code


class Round:
    def _init_(self):
        self.averagePerformance = 0
        self.numPlayersCompleted = 0
        self.backgroundImage = BackgroundImage()
        self.targetImage = []

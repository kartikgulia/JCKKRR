from FirebaseAccess.firebase import db


class BackgroundPicture:
    def _init_(self, document):
        self.targetImage = ''  # TODO
        self.filepath = document['url']
        self.targetDate = document['date']
        self.targetImageCoordinates = [document['BL'],
                                       document['TL'], document['TR'], document['BR']]


class Round:
    # id from array in easy/medium/hard game collection, roundCollection -> collection in database
    def _init_(self, ID, roundCollection):
        self.round_ref = roundCollection.document(ID)
        self.averagePerformance = 0
        self.numPlayersCompleted = 0
        self.backgroundImage = BackgroundPicture(self.round_ref.get())
        self.targetImage = ''  # TODO

    def getData(self):
        # IMPORTANT: target image coords are in order BL, TL, TR, BR
        data = {
            "backgroundImagePath": self.filepath,
            "targetImageCoordinates": self.backgroundImage.targetImageCoordinates,
            "yearTaken": self.backgroundImage.targetDate
        }

from FirebaseAccess.firebase import db


class BackgroundPicture:
    def _init_(self, document):
        # this is in binary so need to reconstruct target image at the frontend
        self.targetImage = document['target']
        self.filepath = document['url']
        self.targetDate = document['date']
        self.targetImageCoordinates = [document['BL'],
                                       document['TL'], document['TR'], document['BR']]


class Round:
    # id from array in easy/medium/hard game collection, roundCollection -> collection in database
    def _init_(self, ID, roundCollection):
        round_ref = roundCollection.document(ID)
        self.averagePerformance = 0
        self.numPlayersCompleted = 0
        self.backgroundImage = BackgroundPicture(self.round_ref.get())
        # this data member feels redundant
        self.targetImage = self.backgroundImage.targetImage

    def getData(self):
        # IMPORTANT: target image coords are in order BL, TL, TR, BR
        # not sure if we are still showing target images but I also returned the target's binary data
        data = {
            "backgroundImagePath": self.backgroundImage.filepath,
            "targetImage": self.targetImage,
            "targetImageCoordinates": self.backgroundImage.targetImageCoordinates,
            "yearTaken": self.backgroundImage.targetDate
        }

        return data

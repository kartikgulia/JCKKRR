from app import db


class BackgroundPicture:
    def _init_(self, document):
        self.targetImage = ''  # TODO
        self.filepath = document['url']
        self.targetDate = document['date']
        # TL, TR, BL, BR (for background currently but idk if we need these. Should use for target)
        self.imageCoordinates = [document['BL'],
                                 document['TL'], document['TR'], document['BR']]


class Round:
    # id from array in easy/medium/hard game collection, difficulty -> EasyRounds, MediumRounds, HardRounds
    def _init_(self, ID, difficulty):
        round_ref = db.collection(difficulty).document(ID)
        self.averagePerformance = 0
        self.numPlayersCompleted = 0
        self.backgroundImage = BackgroundPicture(round_ref.get())
        self.targetImage = ''  # TODO

from FirebaseAccess.firebase import db


class BackgroundPicture:
    def __init__(self, document):
        doc_dictionary = document.to_dict()

        # until kartik and ryan add data to the DB
        if 'url' in doc_dictionary:
            self.filepath = doc_dictionary['url']
            self.targetDate = doc_dictionary['date']
            self.targetImageCoordinates = [doc_dictionary['BL'],
                                           doc_dictionary['TL'], doc_dictionary['TR'], doc_dictionary['BR']]
        else:
            self.filepath = "https://live.staticflickr.com/65535/53483308986_eeb182d542.jpg"
            self.targetDate = 1989
            self.targetImageCoordinates = [[1, 2],
                                           [1, 4], [4, 4], [4, 2]]


class Round:
    # id from array in easy/medium/hard game collection, roundCollection -> collection in database
    def __init__(self, ID, roundCollection):
        round_ref = roundCollection.document(ID)
        self.averagePerformance = 0
        self.numPlayersCompleted = 0
        self.backgroundImage = BackgroundPicture(round_ref.get())

    def getData(self):
        # IMPORTANT: target image coords are in order BL, TL, TR, BR
        data = {
            "backgroundImagePath": self.backgroundImage.filepath,
            "targetImageCoordinates": self.backgroundImage.targetImageCoordinates,
            "yearTaken": self.backgroundImage.targetDate
        }

        return data

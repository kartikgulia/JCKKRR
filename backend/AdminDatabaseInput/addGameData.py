import sys


sys.path.append("")
from FirebaseAccess.firebase import db
import random
from PIL import Image


images_ref = db.collection('images')

# fills the game collections for each difficulty
def createGamesForAllDifficulties(gameCounts):
    difficulties = ["EasyGames", "MediumGames", "HardGames"]
    for difficulty in difficulties:
        for i in range(1, gameCounts[difficulty] + 1):
            gameID = f"Game {i}"
            getImageSet(difficulty, gameID)


def get_randImage():  # gets random image from database
    docs = images_ref.get()
    documents_list = [doc.to_dict() for doc in docs]
    if documents_list:
        random_image_data = random.choice(documents_list)
        return random_image_data
    else:
        return None


# call TargetBgImages to add data for each round
# add round document ids returned from TargetBgImages to rounds array
# send rounds array of round IDs to game collections
# difficulty -> "EasyGames", "HardGames", "MediumGames"
# i -> id for the game document in games. I think i will be the game number (ie Game 1, Game 2....)
def getImageSet(difficulty, i):
    rounds = []
    roundDifficulty = ''

    if (difficulty == "EasyGames"):
        roundDifficulty = "EasyRounds"
    elif (difficulty == "MediumGames"):
        roundDifficulty = "MediumRounds"
    elif (difficulty == "HardGames"):
        roundDifficulty = "HardRounds"

    for j in range(5):
        rounds.append(get_TargetBgImages(roundDifficulty))

    data = {
        "rounds": rounds,
        "gameID": i
    }

    doc_ref = db.collection(difficulty).document(i)
    doc_ref.set(data)


# Gets random image from image collection and sends target, background, date and target coordinates to one of the rounds
# difficulty -> EasyRounds, MediumRounds, HardRounds, i -> round number as id
def get_TargetBgImages(difficulty):
    image_data = get_randImage()
    backgroundImage = image_data['url']
    im = Image.open(image_data['url'])
    width, height = im.size
    dateTaken = image_data["datetaken"]
    dateTaken = dateTaken[0:4]
    if (difficulty == "MediumRounds"):
        TL = (random.randint(1, width-20), random.randint(1, height-20))
        TR = TL + (20, 0)
        BL = TL + (0, 20)
        BR = TL + (20, 20)
    elif (difficulty == "EasyRounds"):
        TL = (random.randint(1, width-20), random.randint(1, height-20))
        TR = TL + (40, 0)
        BL = TL + (0, 40)
        BR = TL + (40, 40)
    else:
        TL = (random.randint(1, width-20), random.randint(1, height-20))
        TR = TL + (10, 0)
        BL = TL + (0, 10)
        BR = TL + (10, 10)

    # backgroundImage.show()
    data = {  # sends dates, filepath for background, and target's corner coordinates
        "url": backgroundImage,
        "TL": TL,
        "TR": TR,
        "BL": BL,
        "BR": BR,
        "date": dateTaken
    }
    # sends data to one of the collections for rounds
    # difficulty -> EasyRounds, MediumRounds, HardRounds
    # got rid of i parameter because I realized we can't have duplicate IDs in a collection. Just going to use image ids as round ids
    doc_ref = db.collection(difficulty).document(image_data['id'])
    doc_ref.set(data)

    # returns image id which we can add to rounds array
    return image_data['id']



def get_images_data():
    docs = images_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict


if __name__ == "__main__":
    gameCounts = "idk"
    createGamesForAllDifficulties(__name__)
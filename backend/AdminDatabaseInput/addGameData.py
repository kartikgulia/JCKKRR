import random
import sys

from PIL import Image

from FirebaseAccess.firebase import db

sys.path.append("")


images_ref = db.collection('images')

# fills the game collections for each difficulty


def createGamesForAllDifficulties(gameCounts):
    difficulties = ["EasyGames", "MediumGames", "HardGames"]
    key = ''
    for difficulty in difficulties:
        start = 1  # added these variables to fix round IDs. Do not worry about these, everything should still be the same
        end = 5

        if difficulty == "EasyGames":
            key = "Easy"
        elif difficulty == "MediumGames":
            key = "Medium"
        else:
            key = "Hard"

        for i in range(1, gameCounts[difficulty] + 1):
            gameID = f"{key}Game {i}"
            getImageSet(difficulty, gameID, start, end)
            start = end + 1
            end = end + 5


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
def getImageSet(difficulty, i, startIndex, endIndex):
    rounds = []
    roundDifficulty = ''

    if (difficulty == "EasyGames"):
        roundDifficulty = "EasyRounds"
    elif (difficulty == "MediumGames"):
        roundDifficulty = "MediumRounds"
    elif (difficulty == "HardGames"):
        roundDifficulty = "HardRounds"

    for j in range(startIndex, endIndex+1):
        rounds.append(get_TargetBgImages(roundDifficulty), j)

    data = {
        "rounds": rounds,
        "gameID": i
    }

    doc_ref = db.collection(difficulty).document(i)
    doc_ref.set(data)


# Gets random image from image collection and sends target, background, date and target coordinates to one of the rounds
# difficulty -> EasyRounds, MediumRounds, HardRounds, i -> round number as id
def get_TargetBgImages(difficulty, i):
    image_data = get_randImage()
    backgroundImage = image_data['url']
    im = Image.open(image_data['url'])
    width, height = im.size
    dateTaken = image_data["datetaken"]
    dateTaken = dateTaken[0:4]
    if (difficulty == "MediumRounds"):
        id = "Medium"
        TL = (random.randint(1, width-20), random.randint(1, height-20))
        TR = TL + (20, 0)
        BL = TL + (0, 20)
        BR = TL + (20, 20)
    elif (difficulty == "EasyRounds"):
        id = "Easy"
        TL = (random.randint(1, width-20), random.randint(1, height-20))
        TR = TL + (40, 0)
        BL = TL + (0, 40)
        BR = TL + (40, 40)
    else:
        id = "Hard"
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

    id = id + "Round" + str(i)
    # sends data to one of the collections for rounds
    # difficulty -> EasyRounds, MediumRounds, HardRounds
    doc_ref = db.collection(difficulty).document(id)
    doc_ref.set(data)

    # returns image id which we can add to rounds array
    return id


def get_images_data():
    docs = images_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict


if __name__ == "__main__":
    gameCounts = "idk"
    createGamesForAllDifficulties(__name__)

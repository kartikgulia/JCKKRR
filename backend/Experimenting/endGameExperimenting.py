
import sys


sys.path.append("backend/")

from FirebaseAccess.firebase import db


players_ref = db.collection('players')


uid = "Praa65tGh3XZvsshV0H3GErZ9Of2"


doc_ref = players_ref.document(uid)


doc = doc_ref.get()



doc_data : dict
if doc.exists:
    doc_data = doc.to_dict()
    print("Document data:", doc_data)


    prevScore = doc_data["score"]
    doc_ref.update({
        "score" : prevScore + 500,
        "gamesPlayed" : ["EasyGame1", "EasyGame2"]
    })


else:
    print("No such document!")


import firebase_admin
from firebase_admin import credentials, firestore



cred = credentials.Certificate('backend\jokerker-d9272-firebase-adminsdk-sbyd5-fda51193ba.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
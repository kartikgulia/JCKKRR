
from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)

# Initialize Firebase
load_dotenv()

# Initialize Firebase with credentials from environment variable
cred = credentials.Certificate(os.getenv('FIREBASE_CREDENTIALS_PATH'))
firebase_admin.initialize_app(cred)
db = firestore.client()
images_ref = db.collection('images')


# Function to retrieve data from Firestore
def get_images_data():
    docs = images_ref.get()
    documents_dict = {}
    for idx, doc in enumerate(docs, start=1):
        documents_dict[idx] = doc.to_dict()
    return documents_dict




@app.route('/')
def hello_world():
    print(get_images_data())
    return 'Hello, World!'


@app.route('/signin', methods=['POST'])
def signin():
    # THIS IS JUST AN EXAMPLE. WE SHOULD NOT HAVE VALIDATION HERE. IT SHOULD BE ANOTHER FUNCTION IN ANOTHER FILE.
    # We would just call it here. This example is just to show u guys how everything works.
    
    # Extract the username and password from the request
    data = request.json
    username = data.get('username')
    password = data.get('password')

    print("Hi Ryan")
    if username == "admin" and password == "password":
        return jsonify({"message": "Successfully signed in"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@app.route('/images', methods=['GET'])
def get_images():
    images_data = get_images_data()
    return jsonify(images_data)


if __name__ == '__main__':
    app.run(port=5000)

import firebase_admin
from firebase_admin import credentials, firestore
import random
import csv


cred = credentials.Certificate('FIREBASE_CREDENTIALS_PATH')
firebase_admin.initialize_app(cred)
db = firestore.client()


images_ref = db.collection('images')


docs = images_ref.get()


documents_dict = {}


for idx, doc in enumerate(docs, start=1):
    documents_dict[idx] = doc.to_dict()


random_document_id = random.choice(list(documents_dict.keys()))
random_document_data = documents_dict[random_document_id]


print("Randomly Selected Document ID:", random_document_id)
print("Randomly Selected Document Data:", random_document_data)



# Function to export data to CSV file
def export_to_csv(data, filename):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=data.keys())
        writer.writeheader()
        writer.writerow(data)

# Export random_document_data to CSV

csv_filename = 'random_document_data.csv'
export_to_csv(random_document_data, csv_filename)

print(f"Random document data has been exported to {csv_filename}.")
import requests
import json

# link to API Documentation: https://www.loc.gov/apis/json-and-yaml/requests/endpoints/

# NOTE: Quality of the images are not great. Need to find another API with better photos
GETrequest = requests.get(
    "https://www.loc.gov/photos/?q=FilePaths&fo=json")

if GETrequest.status_code == 200:
    FilePaths = GETrequest.json()

file = 'FilePaths_JSON'

with open(file, 'w') as json_file:
    json.dump(FilePaths, json_file)

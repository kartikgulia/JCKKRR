import requests
import json

# links to API Documentation:
# https://www.loc.gov/apis/json-and-yaml/requests/endpoints/
# https://unsplash.com/documentation

AccessKey = "OBSBheYhY94ttpR6yi1LeWuHvucFCnYXGzz6IFuCEWw"

# NOTE: Quality of the images are not great. Need to find another API with better photos
# GETrequest = requests.get("https://www.loc.gov/photos/?q=FilePaths&fo=json")

# NOTE: Image Quality is better but not sure if there are historical photos in this API
GETrequest = requests.get(
    f"https://api.unsplash.com/photos/random?client_id={AccessKey}")

FilePaths = GETrequest.json()

file = 'FilePaths_JSON'

with open(file, 'w') as json_file:
    json.dump(FilePaths, json_file)

import requests
import json
import re

# file creates a json file of images from flickr api

# links to API Documentation:
# https://api.flickr.com/services


AccessKey = '2df9cf762ba619075f2827fea8edff89'

GETrequest = requests.get(
    f"https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={AccessKey}&format=json&tags=Historical")

filterJSON = re.search(r'jsonFlickrApi\((.*)\)', GETrequest.text)

# solution to formatting issue with json file returned by flickr
if filterJSON:
    jsonText = filterJSON.group(1)
    filepaths = json.loads(jsonText)

# print(filepaths)
# print(GETrequest.text)
# FilePaths = GETrequest.json()

# for some reason API is not returning the urls to the images. Need to look into this
file = 'ImageData'

with open(file, 'w') as json_file:
    json.dump(filepaths, json_file)

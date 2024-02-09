import requests
import json
import re

# file creates a json file of images from flickr api

# links to API Documentation:
# https://www.flickr.com/services/api/flickr.photos.search.html


def GetJSON():
    AccessKey = '2df9cf762ba619075f2827fea8edff89'
    tags = "The National Archives UK, historical photos"  # search terms
    per_page = 300  # number of images returned
    # min_taken_date = 1950
    # max_taken_date = 1970
    user_id = "35740357@N03"

    GETrequest = requests.get(
        f"https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={AccessKey}&format=json&extras=date_taken&per_page={per_page}&user_id={user_id}")

    filterJSON = re.search(r'jsonFlickrApi\((.*)\)', GETrequest.text)

    # solution to formatting issue with json file returned by flickr
    if filterJSON:
        jsonText = filterJSON.group(1)
        filepaths = json.loads(jsonText)

    # print(filepaths)
    # print(GETrequest.text)

    JSONfile = 'ImageData'

    with open(JSONfile, 'w') as json_file:
        json.dump(filepaths, json_file)

    return JSONfile


def GetURLS(JsonFile):
    # url: https://live.staticflickr.com/{server_id}/{id}_{secret}.jpg

    with open(JsonFile, 'r') as file:
        data = json.load(file)

    photos = data["photos"]["photo"]

    for dict in photos:
        server_id = dict["server"]
        id = dict["id"]
        secret = dict["secret"]
        url = f"https://live.staticflickr.com/{server_id}/{id}_{secret}.jpg"
        dict["url"] = url

    with open(JsonFile, 'w') as file:
        json.dump(data, file)


file = GetJSON()
# print(file)
GetURLS(file)

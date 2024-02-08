import requests
import json
import re

# file creates a json file of images from flickr api

# links to API Documentation:
# https://www.flickr.com/services/api/flickr.photos.search.html


def GetJSON():
    AccessKey = '2df9cf762ba619075f2827fea8edff89'
    tags = "20th century, Old Historical Photography"  # search terms
    per_page = 300  # number of images returned
    # min_taken_date = 1950
    # max_taken_date = 1970

    GETrequest = requests.get(
        f"https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key={AccessKey}&format=json&extras=date_taken,url-l&per_page={per_page}&tags={tags}")

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

    with open('URLS', 'w') as file:
        for dict in photos:
            server_id = dict["server"]
            id = dict["id"]
            secret = dict["secret"]
            url = f"https://live.staticflickr.com/{server_id}/{id}_{secret}.jpg"
            url += '\n'
            file.write(url)


file = GetJSON()
# print(file)
GetURLS(file)

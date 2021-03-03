# https://www.youtube.com/watch?v=yOXQAmYl0Aw&feature=emb_title

import requests
from requests.utils import requote_uri
import json
import pprint

# API Key
api_file = open('api-key.txt', 'r')
api_key = api_file.read()
api_file.close()

# home address input
position = "Kabupaten Purworejo"
query = requote_uri("hotels near " + position)
# base url
url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
send = url + "query=" + query + "&key=" + api_key
# print(send)

# get response
r = requests.get(send) 

# jsoan loads
myjson = json.loads(r.text)
results = myjson['results']

# print(results[0])

no = 1
for i in results:
    i = dict(i)
    print(no)

    for keys, values in i.items():
        print(keys)
    
    no++

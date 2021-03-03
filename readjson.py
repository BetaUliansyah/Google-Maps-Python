import json
import pprint

# load json
myfile = open('results2.txt', 'r')
myjson = myfile.read()
myfile.close()
#myjson = json.loads(myjson)
pprint.pprint(myjson)
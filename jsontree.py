import jsontree

# load json
myfile = open('results-kab purworejo.txt', 'r')
myjson = myfile.read()
myfile.close()

myjson = jsontree(myjson)
print(myjson)
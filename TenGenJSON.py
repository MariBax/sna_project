# from: https://stackoverflow.com/questions/52672598/how-to-read-json-file-containing-objectid-and-isodate-in-python
#Not working
import json
import re

#This will outputs a iterator that converts each file line into a dict.
def readBsonFile(filename):
    with open(filename, "r", encoding= "utf-8-sig") as data_in:
        for line in data_in:
            # convert the TenGen JSON to Strict JSON
            jsondata = re.sub(r'\:\s*\S+\s*\(\s*(\S+)\s*\)',
                              r':\1',
                              line)

            # parse as JSON
            line_out = json.loads(jsondata)

            yield line_out
def from_TenGenJSON(filename):
    with open(filename, "r", encoding='utf-8-sig') as f:
        # read the entire input; in a real application,
        # you would want to read a chunk at a time
        bsondata = '['+f.read()+']'
        # convert the TenGen JSON to Strict JSON
        # here, I just convert the ObjectId and Date structures,
        # but it's easy to extend to cover all structures listed at
        # http://www.mongodb.org/display/DOCS/Mongo+Extended+JSON
        jsondata = re.sub(r'ObjectId\s*\(\s*\"(\S+)\"\s*\)',
                          r'{"$oid": "\1"}',
                          bsondata)
        jsondata = re.sub(r'ISODate\s*\(\s*(\S+)\s*\)',
                          r'{"$date": \1}',
                          jsondata)
        jsondata = re.sub(r'NumberInt\s*\(\s*(\S+)\s*\)',
                          r'{"$numberInt": "\1"}',
                          jsondata)

        # now we can parse this as JSON, and use MongoDB's object_hook
        # function to get rich Python data structures inside a dictionary
        print(jsondata)
        data = json.loads(jsondata.replace("},","pdwekfwe").replace("}","},").replace("pdwekfwe","},"), object_hook=json_util.object_hook)

        return data
for line in readBsonFile(filename="../Posts.json"):
    print(line)
with open("../Posts.json", "r", encoding='utf-8-sig') as file:
    print(file.read())
    posts = json.loads(file.read(), object_hook=json_util.object_hook)#.replace("⭕","")
    
# !pip install pymongo bson
import pandas as pd, networkx as nx
import json, xmljson
from lxml.etree import parse, fromstring, tostring
from xmljson import badgerfish as bf
# <?xml version="1.0" encoding="utf-8" standalone="yes"?>

with open('../Posts.xml','r',encoding="utf-8-sig") as f:
    xml_raw = f.read()
    # print(xml_raw[:400])
    # xml = parse(f)
    
    data = bf.data(fromstring(xml_raw))
#xmljson.badgerfish.data(xml)

data

for d in data["documents"]["document"]:
    d

for doc in data.values():
    print(doc)

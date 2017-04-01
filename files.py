import json
from pprint import pprint

def readParamsFile(path):
    with open(path) as data_file:
        return json.load(data_file)

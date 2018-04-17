import os
import sys
from collections import OrderedDict
import commentjson


class FileBase:
    def __init__(self):
        self.values = dict()

    def load(self, filename, path=None):
        self.values.clear()
        if path is None:
            path = os.getcwd() + "/data"
        path += "/%s.json" % os.path.splitext(filename)[0]

        if not os.path.exists(path):
            print("error: path not exist - ", path)
            sys.exit()

        with open(path, "r") as _file:
            self.values = commentjson.loads(_file.read(), object_pairs_hook=OrderedDict)
        result = "%s loaded" % filename
        return result

    def get(self, key1, key2=None):
        if key2 is None:
            return self.values[key1]
        return self.values[key1][key2]

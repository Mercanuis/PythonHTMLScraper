"""
Simple DB implementation based of this Medium article
https://medium.freecodecamp.org/how-to-write-a-simple-toy-database-in-python-within-minutes-51ff49f47f1
Saves to db.json file provided
"""

import os
import json


class DB(object):
    def __init__(self, location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self, location):
        if os.path.exists(location):
            self._load()
        else:
            self.db = {}
        return True

    def _load(self):
        self.db = json.load(open(self.location, "r"))

    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except Exception as e:
            print("[X] Error Dumping values to Database : " + str(e))
            return False

    def set(self, key, value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
            return True
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self, key):
        try:
            return self.db[key]
        except KeyError:
            print("No Value Can Be Found for " + str(key) + " in DB, need to search")
            return False

    def delete(self, key):
        if key not in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

    def resetdb(self):
        self.db={}
        self.dumpdb()
        return True

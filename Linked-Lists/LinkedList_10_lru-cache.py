# Do not edit the class below except for the insertKeyValuePair,
# getValueFromKey, and getMostRecentKey methods. Feel free
# to add new properties and methods to the class.

# O(1) Time | O(1) Space
class LRUCache:
    def __init__(self, maxSize):
        self.maxSize = maxSize or 1
        self.has_map = {}

    def insertKeyValuePair(self, key, value):
        if len(self.has_map) == self.maxSize and key not in self.has_map:
            del self.has_map[next(iter(self.has_map))]
        self.has_map[key] = value

    def getValueFromKey(self, key):
        if key in self.has_map:
            value = self.has_map[key]
            del self.has_map[key]
            self.has_map[key] = value
        return self.has_map[key] if key in self.has_map else None
        

    def getMostRecentKey(self):
        return next(reversed(self.has_map.keys())) if len(self.has_map) > 0 else None
    

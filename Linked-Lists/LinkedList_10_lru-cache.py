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


# # Do not edit the class below except for the insertKeyValuePair,
# # getValueFromKey, and getMostRecentKey methods. Feel free
# # to add new properties and methods to the class.
# class LRUCache:
#     def __init__(self, maxSize):
#         self.cache = {}
#         self.maxSize = maxSize or 1
#         self.currentSize = 0
#         self.listOfMostRecent = DoubleLinkedList()

#     # O(1) Time | O(1) Space
#     def insertKeyValuePair(self, key, value):
#         if key not in self.cache:
#             if self.currentSize == self.maxSize:
#                 self.evictLeastRecent()
#             else:
#                 self.currentSize += 1
#             self.cache[key] = DoubleLinkedListNode(key, value)
#         else:
#             self.replaceKey(key, value)
#         self.updateMostRecent(self.cache[key])

#     def getValueFromKey(self, key):
#         if key not in self.cache:
#             return None
#         self.updateMostRecent(self.cache[key])
#         return self.cache[key].value

#     # O(1) Time | O(1) Space
#     def getMostRecentKey(self):
#         if self.listOfMostRecent.head is None:
#             return None
#         return self.listOfMostRecent.head.key

#     def evictLeastRecent(self):
#         keyToRemove = self.listOfMostRecent.tail.key
#         self.listOfMostRecent.removeTail()
#         del self.cache[keyToRemove]

#     def updateMostRecent(self, node):
#         self.listOfMostRecent.setHeadTo(node)

#     def replaceKey(self, key, value):
#         if key not in self.cache:
#             raise Exception("The provided key is not in the cache")
#         self.cache[key].value = value


# class DoubleLinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None

#     def setHeadTo(self, node):
#         if self.head == node:
#             return
#         elif self.head is None:
#             self.head = node
#             self.tail = node
#         elif self.head == self.tail:
#             self.tail.prev = node
#             self.head = node
#             self.head.next = self.tail
#         else:
#             if self.tail == node:
#                 self.removeTail()
#             node.removeBindings()
#             self.head.prev = node
#             node.next = self.head
#             self.head = node

#     def removeTail(self):
#         if self.tail is None:
#             return
#         if self.tail == self.head:
#             self.head = None
#             self.tail = None
#             return
#         self.tail = self.tail.prev
#         self.tail.next = None


# class DoubleLinkedListNode:
#     def __init__(self, key, value):
#         self.key = key
#         self.value = value
#         self.prev = None
#         self.next = None

#     def removeBindings(self):
#         if self.prev is not None:
#             self.prev.next = self.next
#         if self.next is not None:
#             self.next.prev = self.prev
#         self.prev = None
#         self.next = None

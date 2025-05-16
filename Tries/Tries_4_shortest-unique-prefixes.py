# O(n * m) time | O(n * m) space - where n is the length of strings, and m
# is the length of the longest string
def shortestUniquePrefixes(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)

    prefixes = []
    for string in strings:
        uniquePrefix = findUniquePrefix(string, trie)
        prefixes.append(uniquePrefix)

    return prefixes

def findUniquePrefix(string, trie):
    currentStringIdx = 0
    currentTrieNode = trie.root

    while currentStringIdx < len(string) - 1:
        currentStringChar = string[currentStringIdx]
        currentTrieNode = currentTrieNode[currentStringChar]
        if currentTrieNode["count"] == 1:
            break
        currentStringIdx += 1

    return string[0 : currentStringIdx + 1]

class Trie:
    def __init__(self):
        self.root = {"count": 0}

    def insert(self, string):
        currentTrieNode = self.root
        for i in range(len(string)):
            if string[i] not in currentTrieNode:
                currentTrieNode[string[i]] = {"count": 0}
            currentTrieNode = currentTrieNode[string[i]]
            currentTrieNode["count"] += 1
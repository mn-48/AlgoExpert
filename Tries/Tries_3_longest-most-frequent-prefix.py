# O(n * m) time | O(n * m) space - where n is the number of strings,
# and m is the length of the longest string
def longestMostFrequentPrefix(strings):
    trie = Trie()
    for string in strings:
        trie.insert(string)
    return trie.maxPrefixFullString[0 : trie.maxPrefixLength]

class Trie:
    def __init__(self):
        self.root = {"count": 0}
        self.maxPrefixCount = 0
        self.maxPrefixLength = 0
        self.maxPrefixFullString = ""
    
    def insert(self, string):
        currentTrieNode = self.root
        for i in range(len(string)):
            if string[i] not in currentTrieNode:
                currentTrieNode[string[i]] = {"count": 0}
            currentTrieNode = currentTrieNode[string[i]]
            currentTrieNode["count"] += 1
            
            if currentTrieNode["count"] > self.maxPrefixCount:
                self.maxPrefixCount = currentTrieNode["count"]
                self.maxPrefixLength = i + 1
                self.maxPrefixFullString = string
            elif (currentTrieNode["count"] == self.maxPrefixCount and 
                  i + 1 > self.maxPrefixLength):
                self.maxPrefixLength = i + 1
                self.maxPrefixFullString = string
# O(s2 * m + s1 * n^2) time | O(s2 * m + s1 * n) space - where s2 is the number
# of substrings, m is the length of the longest substring, s1 is the
# number of strings, and n is the length of the longest string
def stringsMadeUpOfStrings(strings, substrings):
    trie = Trie()
    for substring in substrings:
        trie.insert(substring)

    solutions = []
    for string in strings:
        if isMadeUpOfStrings(string, 0, trie, {}):
            solutions.append(string)

    return solutions


def isMadeUpOfStrings(string, startIdx, trie, memo):
    if startIdx == len(string):
        return True
    if startIdx in memo:
        return memo[startIdx]

    currentTrieNode = trie.root
    for currentCharacterIdx in range(startIdx, len(string)):
        currentCharacter = string[currentCharacterIdx]
        if currentCharacter not in currentTrieNode:
            break

        currentTrieNode = currentTrieNode[currentCharacter]
        if currentTrieNode["isEndOfString"] and isMadeUpOfStrings(
            string, currentCharacterIdx + 1, trie, memo
        ):
            memo[startIdx] = True
            return True

    memo[startIdx] = False
    return False


class Trie:
    def __init__(self):
        self.root = {"isEndOfString": False}

    def insert(self, string):
        currentTrieNode = self.root
        for i in range(len(string)):
            if string[i] not in currentTrieNode:
                currentTrieNode[string[i]] = {"isEndOfString": False}
            currentTrieNode = currentTrieNode[string[i]]
        currentTrieNode["isEndOfString"] = True

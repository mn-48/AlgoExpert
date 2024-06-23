# O(n) Time | O(1) Space

from collections import Counter

def firstNonRepeatingCharacter(string):
    frequencyCount = Counter(string)
    for i in range(len(string)):
        if frequencyCount[string[i]]==1:
            return i
    return -1

if __name__=="__main__":
    ans = firstNonRepeatingCharacter("abcdcaf")
    print(ans)
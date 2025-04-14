#O(n*m) Time | O(m) Space

def commonCharacters(strings):
    return list(set.intersection(*map(set, strings)))


if __name__=="__main__":
    ans = commonCharacters(["abc", "bcd", "cbad"])
    print(ans)
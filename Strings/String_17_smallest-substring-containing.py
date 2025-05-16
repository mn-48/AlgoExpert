# Time	O(N + M)
# Space	O(1)

def smallestSubstringContaining(bigString, smallString):
    hash1 = [0 for _ in range(256)]
    hash2 = [0 for _ in range(256)]
    charCnt = requiredCharCnt = 0

    for i in range(len(smallString)):
        idx = ord(smallString[i])
        if hash1[idx] == 0:
            charCnt += 1
        hash1[idx] += 1

    start = 0
    ans = [-1, -1]

    for i in range(len(bigString)):
        idx = ord(bigString[i])
        hash2[idx] += 1
        if hash2[idx] == hash1[idx]:
            requiredCharCnt += 1

        while charCnt == requiredCharCnt:
            if ans[0] == -1 or i - start + 1 < ans[1] - ans[0] + 1:
                ans = [start, i]
            idx = ord(bigString[start])
            if hash2[idx] - 1 < hash1[idx]:
                break
            start += 1
            hash2[idx] -= 1

    return bigString[ans[0] : ans[1] + 1]

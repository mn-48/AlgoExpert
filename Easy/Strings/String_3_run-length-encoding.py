# O(n) Time | O(n) space

def runLengthEncoding(string):
    encodingStr = ""
    cnt = 1

    for i in range(1, len(string)):
        prevChar = string[i-1]
        currChar = string[i]
        if currChar != prevChar or cnt ==9:
            encodingStr += f"{cnt}{prevChar}"
            cnt=0
        cnt += 1
    encodingStr += f"{cnt}{string[-1]}" #Do it for last char

    return encodingStr
    

if __name__=="__main__":
    ans = runLengthEncoding("AAAAAAAAAAAAABBCCCCDD")
    print(ans)
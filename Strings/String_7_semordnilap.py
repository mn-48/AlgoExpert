

# O(n*m) Time | O(m*n) Space
def semordnilap(words):
    ans = []

    while words:
        w = words.pop(0)
        if w[::-1] in words:
            ans.append([w, w[::-1]])
            words.remove(w[::-1])

    return ans
       
if __name__=="__main__":
    input = ["desserts", "stressed", "hello"]
    ans = semordnilap(input)
    print(ans)
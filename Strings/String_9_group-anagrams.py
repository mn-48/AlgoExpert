# O(w*n*lon(n)) Time | O(wn) Space

def groupAnagrams(words):
    groups = {}

    for word in words:
        sorted_text = ''.join(sorted(word))
        if sorted_text in groups:
            groups[sorted_text].append(word)
        else:
            groups[sorted_text] = [word]
    return list(groups.values())

    # res = []
    # for group, value in groups.items():
    #     res.append(value)
    # return res


if __name__ == "__main__":
    words = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
    sol = groupAnagrams(words)
    print(sol)

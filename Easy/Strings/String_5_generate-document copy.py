# O(n*m) Time | O(c) Space

from collections import Counter
def generateDocument(characters, document):
    # Write your code here.
    return Counter(document)-Counter(characters) == {}


if __name__=="__main__":
    characters = "Bste!hetsi ogEAxpelrt x "
    document = "AlgoExpert is the Best!"
    ans = generateDocument(characters, document)
    print(ans)
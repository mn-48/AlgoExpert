
# (2n)!/ (n!*(n+1)!) Time | (2n)!/ (n!*(n+1)!) Space
def generateDivTags(numberOfTags):
    matchDivTags = []
    generateDivTagsFromPrefix(numberOfTags, numberOfTags, "", matchDivTags)
    
    return matchDivTags
def generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded, prefix, result):
    if openingTagsNeeded>0:
        newPrefix = prefix+"<div>"
        generateDivTagsFromPrefix(openingTagsNeeded-1, closingTagsNeeded, newPrefix, result)

    if openingTagsNeeded<closingTagsNeeded:
        newPrefix = prefix+"</div>"
        generateDivTagsFromPrefix(openingTagsNeeded, closingTagsNeeded-1, newPrefix, result)

    if closingTagsNeeded ==0:
        result.append(prefix)
        
if __name__=="__main__":
    ans = generateDivTags(3)
    print(ans)
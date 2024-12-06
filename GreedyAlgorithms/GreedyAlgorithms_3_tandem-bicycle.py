# Time O(nlog(n)) | Space O(1) 


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort(reverse=fastest)
    
    total = 0
    for i in range(len(redShirtSpeeds)):

        total+= max(redShirtSpeeds[i],blueShirtSpeeds[i])
   
    return total

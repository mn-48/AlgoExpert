# Time O(nlog(n)) | Space O(1) 


def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)
    
    
    is_red_taller = redShirtHeights[0] >  blueShirtHeights[0]
    
    for i in range(len(redShirtHeights)):
        if is_red_taller:
            if blueShirtHeights[i] >= redShirtHeights[i]:
                return False
            
        else:
             if redShirtHeights[i] >= blueShirtHeights[i]:
                return False
            
    return True

# O(n) Time | O(1) Space

def threeNumberSort(array, order):
    index = 0
    for i in range(2):
        val = order[i]
        for j in range(len(array)):
            if array[j] == val:
                array[j], array[index] = array[index], array[j]
                index +=1
    return array
   
if __name__=="__main__":
    array = [1, 0, 0, -1, -1, 0, 1, 1]
    order = [0, 1, -1]
    ans = threeNumberSort(array, order)
    print(ans)
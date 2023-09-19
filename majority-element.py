def majorityElement(array):
    ans = array[0]
    cnt = 1

    for i in range(1, len(array)):
        if ans == array[i]:
            cnt +=1
        else:
            cnt -=1
        if cnt ==0:
            ans = array[i]
            cnt = 1
    # Write your code here.
    return ans

array = [1, 2, 3, 2, 2, 1, 2]
print(majorityElement(array))
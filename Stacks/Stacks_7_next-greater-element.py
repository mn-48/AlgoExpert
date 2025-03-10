# O(n) Time | O(n) Space
def nextGreaterElement(array):
    n = len(array)
    res = [-1] * n
    stack = []
    

    for idx in range(2*n-1, -1, -1):
        circularIdx = idx % n
        while len(stack) > 0:
            if stack[len(stack)-1] <= array[circularIdx]:
                stack.pop()
            else:
                res[circularIdx] = stack[len(stack)-1]
                break
        stack.append(array[circularIdx])
    return res
                
if __name__=="__main__":
    input = [2, 5, -3, -4, 6, 7, 2]
    sol = nextGreaterElement(input)
    print(sol)

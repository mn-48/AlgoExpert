
# O(n) Time | O(n) Space

def bestDigits(number, numDigits):
    stack = []
    for digit in number:
        while  numDigits > 0 and len(stack)> 0 and digit > stack[len(stack)-1]:
            numDigits -= 1
            stack.pop()
        stack.append(digit)

    while numDigits > 0:
        numDigits -= 1
        stack.pop()
    return "".join(stack)


if __name__=="__main__":

    ans = bestDigits("462839", 2)
    print(ans)

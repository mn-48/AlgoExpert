# O(n) Time | O(n) Space
def reversePolishNotation(tokens):
    stack = []
    for token in tokens:
        if token == "+":
            stack.append(stack.pop() + stack.pop())
        elif token == "-":
            firstNum = stack.pop()
            stack.append(stack.pop() - firstNum)
        elif token =="*":
            stack.append(stack.pop() * stack.pop())
            
        elif token=="/":
            firstNum = stack.pop()
            stack.append(int(stack.pop() / firstNum))
        else:
            stack.append(int(token))
    return stack.pop()

if __name__=="__main__":
    input = ["3", "2", "+", "7", "*"]
    sol = reversePolishNotation(input)
    print(sol)

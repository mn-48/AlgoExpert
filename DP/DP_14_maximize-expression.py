# O(n) Time | O(1) Space
def maximizeExpression(array):
    # Write your code here.
    if len(array) < 4:
        return 0
    a= b = c = d = float('-inf')
    for x in array:
        A = max(a, x)
        B = max(b, a-x)
        C = max(c, b+x)
        D = max(d, c-x)
        a, b, c, d = A, B, C, D
    return d

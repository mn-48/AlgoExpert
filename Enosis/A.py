# python A.py < test.in > test.out
# touch A.py B.py C.py D.py E.py test.in test.out

# square_positive = lambda x: x**2 if x > 0 else x

def lambdaMap(arr):
    a = list(filter(lambda x: x>0, row) for row in arr)
    square_positive = lambda x: x**2 
    ans = [list(map(square_positive, row)) for row in a]
    return ans


if __name__ == '__main__':
    n = int(raw_input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, raw_input().split())))
    
    ans = lambdaMap(arr)
    for row in ans:
        print(' '.join(map(str, row)))

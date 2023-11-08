#  Time O(v+e) | Space O(1)

def waterfallStreams(array, source):
    w, h = len(array), len(array[0])

    def valid_point(x,y):
        return (x>=0 and x< w) and (y>=0 and y<h)
    
    def helper(pt, percentage, direction):
        (x, y) = pt
        if not valid_point(x,y): return
        if array[x][y]==1: return

        array[x][y] += percentage

        if x == w-1: return

        if array[x+1][y] <= 0:
            helper((x+1, y), percentage, 'D')
        else:
            if direction=='R':
                helper((x, y+1), percentage, 'R')
            elif direction=='L':
                helper((x, y-1), percentage, 'L')
            else:
                helper((x, y+1), percentage/2, 'R')
                helper((x, y-1), percentage/2, 'L')

    helper((0, source), -100, 'D')
    return [-x for x in array[-1]]



if __name__=="__main__":
    array = [
        [0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [1, 1, 1, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0],
        ]
    source = 3

    print(waterfallStreams(array, source))


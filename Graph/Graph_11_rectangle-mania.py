
#  O(m*n) | O(n)

def rectangleMania(coords):
    # Write your code here.
    coords_set = set([(x, y) for x, y in coords])

    cnt = 0

    for x1, y1 in coords:
        for x2, y2 in coords:
            if x2<=x1 or y2<=y1:
                continue
            if (x1, y2) in coords_set and (x2, y1) in coords_set:
                cnt +=1
    return cnt
if __name__=="__main__":
    coords = [[0, 0], [0, 1], [1, 1], [1, 0], [2, 1], [2, 0], [3, 1], [3, 0]]
        
    ans = sol()
    print(ans)
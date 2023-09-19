# O(n) Time | O(1) Space

from itertools import combinations

def countScures(points):
    num_squire = 0

    for (p1, p2) in combinations(points,2):
        # print(p1, p2)
        '''
        [1, 1] [0, 0]
        [1, 1] [0, 1]
        [1, 1] [1, 0]
        [0, 0] [0, 1]
        [0, 0] [1, 0]
        [0, 1] [1, 0]                                                   
        '''

        # mid = [(x1+x2)/2, (y1+y2)/2]
        mid = [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2]
        # print('mid: ', mid)
        x_distance, y_distance = p1[0]-mid[0] , p1[1]-mid[1]
        # print("x_distance, x_distance: ", x_distance, x_distance)

        x_offset_1, y_offset_1 = mid[0] - y_distance, mid[1]+ x_distance
        x_offset_2, y_offset_2 = mid[0] + y_distance, mid[1]- x_distance

        if [x_offset_1, y_offset_1] in points and [ x_offset_2, y_offset_2] in points:
            num_squire += 1
    return num_squire//2


# points = [[1, 1], [0, 0], [0, 1], [1, 0]]

# print(countScures(points))
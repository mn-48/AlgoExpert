# O(n^2) Time | O(n) Space

from fractions import Fraction

def lineThroughPoints(points):
    max_lines_through_points = 1
    for i in range(len(points)-1):
        x1, y1 = points[i]
        slopes = {}

        for j in range(i+1, len(points)):
            x2, y2 = points[j]

            slope = Fraction(y2-y1, x2-x1) if x1 != x2 else float("inf")

            numerator, denominator = (1, 0) if slope == float("inf") else (slope.numerator, slope.denominator)

            if (numerator, denominator) not in slopes:
                slopes[(numerator, denominator)] = 1
            slopes[(numerator, denominator)] += 1
        max_lines_through_current_pivot = max(slopes.values())
        max_lines_through_points = max(max_lines_through_points, max_lines_through_current_pivot)

    return max_lines_through_points


 

points =[
  [1, 1],
  [2, 2],
  [3, 3],
  [0, 4],
  [-2, 6],
  [4, 0],
  [2, 1]
]

print(lineThroughPoints(points))
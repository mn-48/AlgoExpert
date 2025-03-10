def collidingAsteroids(asteroids):

    stack = []
    for asteroid in asteroids:
        if not stack or asteroid > 0:
            stack.append(asteroid)
        else:
            while stack and stack[-1] > 0:
                if abs(stack[-1]) == abs(asteroid):
                    stack.pop()
                    break
                elif abs(stack[-1]) > abs(asteroid):
                    break
                else:
                    stack.pop()
            else:
                stack.append(asteroid)

    return stack
    
if __name__=="__main__":
    input = [-3, 5, -8, 6, 7, -4, -7]
    sol = collidingAsteroids(input)
    print(sol)





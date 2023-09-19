# O(n) Time | O(n) Space

def minRewards(scores):
    # Write your code here.
    n = len(scores)
    rewards = [1]*n

    for i in range(n-1):
        if scores[i] < scores[i+1]:
            rewards[i+1] = rewards[i]+1
    for i in reversed(range(1,n)):
        if scores[i-1] > scores[i]:
            rewards[i-1] = max(rewards[i]+1, rewards[i-1])
    return sum(rewards)



scores = [8, 4, 2, 1, 3, 6, 7, 9, 5]
print(minRewards(scores))

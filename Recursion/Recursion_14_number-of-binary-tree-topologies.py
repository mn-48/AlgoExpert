# O(n^2) Time | O(n) Space

def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    if n<=1:
        return 1
    dp = [0] *(n+1)
    dp[0] = dp[1] = 1
    for i in range(2, n+1):
        for j in range(i):
            dp[i] += dp[j] * dp[i-j-1]
    return dp[n]

if __name__=="__main__":
    ans = numberOfBinaryTreeTopologies(20)
    print(ans)
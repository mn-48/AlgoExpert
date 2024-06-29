# Time O(nlog(n)) | Space O(1) 

def minimumWaitingTime(queries):
    queries = sorted(queries, reverse=True)
    total = 0
    for i in range(len(queries)):
        total += i * queries[i]
    return total


if __name__=="__main__":
    queries = [3,2,1,2,6]
    ans = minimumWaitingTime(queries)
    print(ans)

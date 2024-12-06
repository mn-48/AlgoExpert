# Time O(nlog(n)) | Space O(1) 

def optimalFreelancing(jobs):
    length_of_week = 7
    profit = 0
    jobs.sort(key=lambda job: job['payment'], reverse=True)
    time_line  = [False] * length_of_week
    
    # print(jobs)
    for job in jobs:
        max_time = min(job['deadline'], length_of_week,)
        for time in reversed(range(max_time)):
            if time_line[time] == False:
                time_line[time] = True
                profit += job['payment']
                break
                
    return profit



if __name__=="__main__":
    jobs = [
        {"deadline": 1, "payment": 1},
        {"deadline": 2, "payment": 1},
        {"deadline": 2, "payment": 2},
    ]
    ans = optimalFreelancing(jobs)
    print(ans)
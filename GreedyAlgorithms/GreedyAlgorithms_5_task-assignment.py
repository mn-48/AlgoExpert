#  O(nlog(n)) Time | O(n) Space

def taskAssignment(k, tasks):
    sorted_task = sorted(list(enumerate(tasks)), key = lambda x : x[1])

    # print(sorted_task)

    task_pairs = []
    for i in range(k):
        task_pairs.append([sorted_task[i][0], sorted_task[len(tasks)-1-i][0]])
    return task_pairs


if __name__=="__main__":
    k = 3
    tasks = [1, 3, 5, 3, 1,4]
    ans = taskAssignment(k, tasks)
    print(ans)
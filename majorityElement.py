def majorityElement(nums):
    len_nums = len(nums) + 2
    seen = [i+1 for i in  range(len_nums)]

    for i in nums:
        seen[i-1] *= -1

    missing = []
    for i in seen:
        if i>0:
            missing.append(i)
    return missing

nums = [1,2,3]
print(majorityElement(nums))
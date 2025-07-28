lst=[6,3,5,8,4,7,3]
sum=9
nums={}

def get_nums():
    for i in range(len(lst)):
        diff = sum - lst[i]
        if nums.get(diff):
            return nums.get(diff), i
        nums[lst[i]] = i
        print(nums)
    return None

print(get_nums())


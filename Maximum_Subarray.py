def max_subarray(nums):
    max_sum = current_sum = nums[0]
    start = end = s = 0  # For tracking subarray indices

    for i in range(1, len(nums)):
        #print(f"\ni={i}, current_sum={current_sum}, max_sum={max_sum}, start={start}, end={end}")
        if nums[i] > current_sum + nums[i]:
            current_sum = nums[i]
            s = i  # potential new start
        else:
            current_sum += nums[i]

        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i
        #print(f"i={i}, current_sum={current_sum}, max_sum={max_sum}, start={start}, end={end}")
    return max_sum, nums[start:end+1]  # Return both sum and subarray

# Test
# [-2, 1, -3, 2, -1, 4, 1, -5, 4], [7,-5,2,-2,5,6,2,-1]
nums = [-2, 1, -3, 2, -1, 4, 1, -5, 4]
result = max_subarray(nums)
print("Max Sum:", result[0])
print("Subarray:", result[1])



# O(n^2)

"""def sub_array(arr):
    start = end = 0
    mx = arr[0]
    n=len(arr)
    for i in range(n):
        cumx = 0
        for j in range(i, n):
            cumx=cumx+arr[j]
            if cumx>mx:
                mx = cumx
                start = i
                end = j
            
                
            
    return arr[start:end+1], mx
    
if __name__ == "__main__":
    arr = [7,-5,2,-2,5,6,2,-1]
    arr1, mx = sub_array(arr)
    print(f"Array is : {arr1}")
    print(f"Max sum is {mx}")

"""
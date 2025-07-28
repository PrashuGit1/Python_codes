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
nums = [7,-5,2,-2,5,6,2,-1]
result = max_subarray(nums)
print("Max Sum:", result[0])
print("Subarray:", result[1])
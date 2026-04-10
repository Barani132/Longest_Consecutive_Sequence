#Longest Consecutive Sequence

arr = [100,4,200,1,3,2]

nums = set(arr)
longest = 0

for num in nums:
    if num - 1 not in nums:
        length = 1
        while num + length in nums:
            length += 1
        longest = max(longest, length)

print("Longest:", longest)

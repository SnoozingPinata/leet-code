
# Runtime: 2552 ms, faster than 30.28% of Python3 online submissions for Two Sum.
# Memory Usage: 14.9 MB, less than 80.65% of Python3 online submissions for Two Sum.

def TwoSum(nums, target):
    length_of_nums = len(nums)
    for i in range(0, length_of_nums):
        difference = target - nums[i]
        for index in range(i + 1, length_of_nums):
            if nums[index] == difference:
                return i, index


# I expected this to be faster, but oh well...
# Runtime: 4155 ms, faster than 16.17% of Python3 online submissions for Two Sum.
# Memory Usage: 15 MB, less than 65.50% of Python3 online submissions for Two Sum.
def TwoSum_v2(nums, target):
    index1 = 0
    index2 = 0
    while True:
        difference = target - nums[index1]
        index2 = index1 + 1
        while True:
            try:
                if nums[index2] == difference:
                    return index1, index2
                index2 += 1
            except IndexError:
                break
        index1 += 1


nums = [-1,-2,-3,-4,-5]
target = -8
print(TwoSum(nums, target))
print(TwoSum_v2(nums, target))
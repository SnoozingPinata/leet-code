
# Runtime: 110 ms, faster than 65.99% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 14.1 MB, less than 68.55% of Python3 online submissions for Median of Two Sorted Arrays.
class Solution:
    def __init__(self):
        pass

    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        merged_array = self.MergeArrays(nums1, nums2)
        if self.isEven(len(merged_array)):
            return self.GetMedianOfEvenArray(merged_array)
        else:
            return self.GetMedianOfOddArray(merged_array)

    def MergeArrays(self, array1, array2):
        merged_array = []
        for val in array1:
            merged_array.append(val)
        for val in array2:
            merged_array.append(val)
        merged_array.sort()
        return merged_array

    def isEven(self, number):
        if number % 2 == 0:
            return True
        return False

    def GetMedianOfEvenArray(self, array):
        second_num_index = len(array) // 2
        first_num_index = second_num_index - 1
        return (array[first_num_index] + array[second_num_index]) / 2

    def GetMedianOfOddArray(self, array):
        mid_index = len(array) // 2
        return array[mid_index]


if __name__ == "__main__":
    solver = Solution()
    odd_array = [1, 2, 3, 4, 5]
    print(solver.GetMedianOfOddArray(odd_array))
    even_array = [1, 2, 3, 4, 5, 6]
    print(solver.GetMedianOfEvenArray(even_array))
    print(solver.isEven(len(odd_array)))
    print(solver.isEven(len(even_array)))

    nums1 = [1, 2]
    nums2 = [3, 4]
    print(solver.findMedianSortedArrays(nums1, nums2))
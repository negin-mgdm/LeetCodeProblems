'''
Given an array of integers nums which is sorted in ascending order, 
and an integer target, write a function to search target in nums. 
If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4

Example 2:
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 
Constraints:
1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid_index = (start + end) // 2

            if nums[mid_index] == target:
                return mid_index

            elif nums[mid_index] < target:
                start = mid_index + 1

            else:
                end = mid_index - 1

        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
solution = Solution()
print(solution.search(nums, target))


class Solution(object):
    def search1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i, num in enumerate(nums):
            if num == target:
                return i
        return -1


nums = [-1, 0, 3, 5, 9, 12]
target = 9
solution = Solution()
print(solution.search1(nums, target))

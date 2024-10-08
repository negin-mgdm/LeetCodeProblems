'''
You are given an integer array nums with the following properties:
nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

Example 1:
Input: nums = [1,2,3,3]
Output: 3

Example 2:
Input: nums = [2,1,2,5,3,2]
Output: 2

Example 3:
Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
 
Constraints:
2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 104
nums contains n + 1 unique elements and one of them is repeated exactly n times.
'''
# First solution

from collections import Counter


class Solution(object):
    def repeatedNTimes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = Counter(nums)
        for key, value in count.items():
            if value > 1:
                return key


nums = [2, 1, 2, 5, 3, 2]
solution = Solution()
print(solution.repeatedNTimes(nums))


# Second Solution

class Solution(object):
    def repeatedNTimes1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen_nums = set()
        for num in nums:
            if num not in seen_nums:
                seen_nums.add(num)
            else:
                return num


nums = [2, 1, 2, 5, 3, 2]
solution = Solution()
print(solution.repeatedNTimes1(nums))

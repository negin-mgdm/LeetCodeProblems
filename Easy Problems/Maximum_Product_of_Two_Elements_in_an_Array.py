'''
Given the array of integers nums, you will choose two different indices i and j of that array. 
Return the maximum value of (nums[i]-1)*(nums[j]-1).
 
Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, 
that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12. 

Example 2:
Input: nums = [1,5,4,5]
Output: 16
Explanation: Choosing the indices i=1 and j=3 (indexed from 0), you will get the maximum value of (5-1)*(5-1) = 16.

Example 3:
Input: nums = [3,7]
Output: 12

Constraints:
2 <= nums.length <= 500
1 <= nums[i] <= 10^3
'''


# Solution 1
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums, reverse=True)

        result = (sorted_nums[0]-1) * (sorted_nums[1]-1)

        return result


nums = [3, 4, 5, 2]
solution = Solution()
print(solution.maxProduct(nums))


# Solution 2
class Solution(object):
    def maxProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        products = []

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    calc = (nums[i]-1) * (nums[j]-1)
                    products.append(calc)

        return max(products)


nums = [3, 4, 5, 2]
solution = Solution()
print(solution.maxProduct1(nums))

'''
Given an integer n, return any array containing n unique integers such that they add up to 0.

Example 1:
Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].

Example 2:
Input: n = 3
Output: [-1,0,1]

Example 3:
Input: n = 1
Output: [0]
 
Constraints:
1 <= n <= 1000
'''


class Solution(object):
    def sumZero(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        x = n//2
        negative_nums = list(range(-x, 0))
        positive_nums = list(range(1, x+1))

        nums = negative_nums + positive_nums

        if n % 2 != 0:
            nums.append(0)

        return nums


n = 5
solution = Solution()
print(solution.sumZero(n))

'''
A self-dividing number is a number that is divisible by every digit it contains.
For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
A self-dividing number is not allowed to contain the digit zero.
Given two integers left and right, return a list of all the self-dividing numbers in the range [left, right] (both inclusive).

Example 1:
Input: left = 1, right = 22
Output: [1,2,3,4,5,6,7,8,9,11,12,15,22]

Example 2:
Input: left = 47, right = 85
Output: [48,55,66,77]
 
Constraints:
1 <= left <= right <= 104
'''


class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for num in range(left, right + 1):
            valid = True
            for digit in str(num):
                if digit == '0' or num % int(digit) != 0:
                    valid = False
                    break
            if valid:
                result.append(num)
        return result


left = 47
right = 85
solution = Solution()
print(solution.selfDividingNumbers(left, right))

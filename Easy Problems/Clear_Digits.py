'''
You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.
Note that the operation cannot be performed on a digit that does not have any non-digit character to its left.

Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the string.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".

Constraints:
1 <= s.length <= 100
s consists only of lowercase English letters and digits.
The input is generated such that it is possible to delete all digits.
'''


class Solution(object):
    def clearDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        i = 0

        while i < len(s):
            if s[i].isdigit():
                j = i - 1
                while j >= 0 and s[j] == "":
                    j -= 1
                if j >= 0:
                    s[j] = ""

                s[i] = ""
            i += 1

        return "".join(s)


s = "cb34s22wr"
solution = Solution()
print(solution.clearDigits(s))

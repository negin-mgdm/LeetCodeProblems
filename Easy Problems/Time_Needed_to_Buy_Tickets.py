'''
There are n people in a line queuing to buy tickets, where the 0th person is at the front of the line and the (n - 1)th person
is at the back of the line.

You are given a 0-indexed integer array tickets of length n where the number of tickets that the ith person would like to 
buy is tickets[i].

Each person takes exactly 1 second to buy a ticket. A person can only buy 1 ticket at a time and 
has to go back to the end of the line (which happens instantaneously) in order to buy more tickets. 
If a person does not have any tickets left to buy, the person will leave the line.

Return the time taken for the person at position k (0-indexed) to finish buying tickets.

Example 1:
Input: tickets = [2,3,2], k = 2
Output: 6
Explanation: 
- In the first pass, everyone in the line buys a ticket and the line becomes [1, 2, 1].
- In the second pass, everyone in the line buys a ticket and the line becomes [0, 1, 0].
The person at position 2 has successfully bought 2 tickets and it took 3 + 3 = 6 seconds.

Example 2:
Input: tickets = [5,1,1,1], k = 0
Output: 8
Explanation:
- In the first pass, everyone in the line buys a ticket and the line becomes [4, 0, 0, 0].
- In the next 4 passes, only the person in position 0 is buying tickets.
The person at position 0 has successfully bought 5 tickets and it took 4 + 1 + 1 + 1 + 1 = 8 seconds.

Constraints:
n == tickets.length
1 <= n <= 100
1 <= tickets[i] <= 100
0 <= k < n
'''


class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        count = 0

        while len(tickets) != 0:
            if tickets[k] == 1 and k == 0:
                break

            x = tickets.pop(0)

            if x != 1:
                x -= 1
                tickets.append(x)

            count += 1

            if k == 0:
                k = len(tickets) - 1
            else:
                k -= 1

        return count + 1


tickets = [2, 3, 2]
k = 2
solution = Solution()
print(solution.timeRequiredToBuy(tickets, k))

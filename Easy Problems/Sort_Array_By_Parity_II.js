/*
Given an array of integers nums, half of the integers in nums are odd, and the other half are even.
Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.
Return any answer array that satisfies this condition.

Example 1:
Input: nums = [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

Example 2:
Input: nums = [2,3]
Output: [2,3]
 
Constraints:
2 <= nums.length <= 2 * 104
nums.length is even.
Half of the integers in nums are even.
0 <= nums[i] <= 1000
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortArrayByParityII = function (nums) {
    let evenNums = [];
    let oddNums = [];

    for (let num of nums) {
        if (num % 2 == 0) {
            evenNums.push(num);
        } else {
            oddNums.push(num);
        }
    }

    let result = [];

    for (let i = 0; i < nums.length; i++) {
        if (i % 2 == 0) {
            result.push(evenNums[0]);
            evenNums.shift();
        } else {
            result.push(oddNums[0]);
            oddNums.shift();
        }
    }
    return result;
};

let nums = [4, 2, 5, 7];
console.log(sortArrayByParityII(nums));
/*
You are given a string title consisting of one or more words separated by a single space, where each word consists of English letters. 
Capitalize the string by changing the capitalization of each word such that:

If the length of the word is 1 or 2 letters, change all letters to lowercase.

Otherwise, change the first letter to uppercase and the remaining letters to lowercase.
Return the capitalized title.

Example 1:
Input: title = "capiTalIze tHe titLe"
Output: "Capitalize The Title"
Explanation:
Since all the words have a length of at least 3, the first letter of each word is uppercase, and the remaining letters are lowercase.

Example 2:
Input: title = "First leTTeR of EACH Word"
Output: "First Letter of Each Word"
Explanation:
The word "of" has length 2, so it is all lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, 
and the remaining letters are lowercase.

Example 3:
Input: title = "i lOve leetcode"
Output: "i Love Leetcode"
Explanation:
The word "i" has length 1, so it is lowercase.
The remaining words have a length of at least 3, so the first letter of each remaining word is uppercase, 
and the remaining letters are lowercase.
 
Constraints:
1 <= title.length <= 100
title consists of words separated by a single space without any leading or trailing spaces.
Each word consists of uppercase and lowercase English letters and is non-empty.
*/

/**
 * Capitalizes the first letter of a string and converts the rest to lowercase.
 * @param {string} str - The input string.
 * @return {string} - The capitalized string.
 */
function capitalize(str) {
    if (str.length === 0) return str;
    return str.charAt(0).toUpperCase() + str.slice(1).toLowerCase();
}

/**
 * @param {string} title
 * @return {string}
 */
var capitalizeTitle = function (title) {
    let words = title.split(" ");
    let newTitle = "";
    for (let word of words) {
        if (word.length > 2) {
            newTitle += capitalize(word) + " ";
        } else {
            newTitle += word.toLowerCase() + " ";
        }
    }
    return newTitle.trim();
};

let title = "i lOve leetcode";
console.log(capitalizeTitle(title));
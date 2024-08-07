/*
You own a Goal Parser that can interpret a string command. 
The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

Example 1:
Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".

Example 2:
Input: command = "G()()()()(al)"
Output: "Gooooal"

Example 3:
Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 
Constraints:
1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
*/


/**
 * @param {string} command
 * @return {string}
 */
var interpret = function (command) {
    return command.replace(/\(\)/g, "o").replace(/\(al\)/g, "al");
};

let command = "(al)G(al)()()G";
console.log(interpret(command));

/*
 * @param {string} command
 * @return {string}
 
var interpret = function (command) {
    let result = "";
    let x = "";

    for (let i of command) {
        if (i == "G") {
            result += i;
        } else {
            x += i;
        }
        if (x == "()") {
            result += "o";
            x = "";
        } else if (x == "(al)"){
            result += "al";
            x = "";
        }
    }
    return result;
};

let command = "(al)G(al)()()G";
console.log(interpret(command));
*/
'''
1678. Goal Parser Interpretation
Solved
Easy
Topics
Companies
Hint

You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.
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
'''

class Solution:
    def interpret(self, command: str) -> str:
        new_str = ""
        for index_char, character in enumerate(command):
            if character == "G":
                new_str += "G"
            elif character == "(":
                if command[index_char+1] == ")":
                    new_str += "o"
                elif command[index_char+1] == "a":
                    new_str += "al"
            else:
                continue
        return new_str
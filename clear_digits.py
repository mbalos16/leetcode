'''
3174. Clear Digits
Solved
Easy
Topics
Companies
Hint

You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
    Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

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

class Solution:
    def clearDigits(self, s: str) -> str:
        list_of_digits = ['0', '1', '2', '3', '4','5', '6', '7', '8', '9']
        new_s = ''
        for index_char, char in enumerate(s):
            if char in list_of_digits:
                new_s = new_s[:-1]
            else:
                new_s += char
        return new_s

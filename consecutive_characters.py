'''
1446. Consecutive Characters
Solved
Easy
Topics
Companies
Hint

The power of the string is the maximum length of a non-empty substring that contains only one unique character.

Given a string s, return the power of s.


Example 1:
Input: s = "leetcode"
Output: 2
Explanation: The substring "ee" is of length 2 with the character 'e' only.

Example 2:
Input: s = "abbcccddddeeeeedcba"
Output: 5
Explanation: The substring "eeeee" is of length 5 with the character 'e' only.

 
Constraints:
    1 <= s.length <= 500
    s consists of only lowercase English letters.

'''
class Solution:
    def maxPower(self, s: str) -> int:
        max_len = 0
        last_char = ""
        last_char_count = 0
        for char in s:
            if char == last_char:
                last_char_count +=1
            else:
                last_char = char
                last_char_count =1
            if last_char_count > max_len:
                    max_len = last_char_count
        return max_len
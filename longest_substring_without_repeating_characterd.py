'''
3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
Companies
Hint

Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

 

Constraints:

    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.


'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_char = []
        longest_substring = 0
        for char in s:
            if char not in seen_char:
                seen_char.append(char)
                if len(seen_char) > longest_substring:
                    longest_substring = len(seen_char)
            else:
                seen_char.append(char)
                old_char = seen_char.index(char)
                seen_char = seen_char[old_char+1:]
        return longest_substring
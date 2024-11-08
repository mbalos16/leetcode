'''
796. Rotate String
Solved
Easy
Topics
Companies

Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character of s to the rightmost position.
    For example, if s = "abcde", then it will be "bcdea" after one shift.

 
Example 1:
Input: s = "abcde", goal = "cdeab"
Output: true

Example 2:
Input: s = "abcde", goal = "abced"
Output: false

Constraints:
    1 <= s.length, goal.length <= 100
    s and goal consist of lowercase English letters.

Seen this question in a real interview before?
1/5
Yes
No
Accepted
515K
Submissions
816.9K
'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            new_s = s[i:]+ s[:i]
            if new_s == goal:
                return True
        return False
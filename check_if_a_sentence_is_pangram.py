'''
1832. Check if the Sentence Is Pangram
Easy
Topics
Companies
Hint

A pangram is a sentence where every letter of the English alphabet appears at least once.
Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.

Example 1:
Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

Example 2:
Input: sentence = "leetcode"
Output: false

Constraints:
    1 <= sentence.length <= 1000
    sentence consists of lowercase English letters.
'''

import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = set(string.ascii_lowercase)
        for char in sentence:
            try:
                alphabet.remove(char)
            except: KeyError("Item alredy removed")
        return len(alphabet) == 0
        
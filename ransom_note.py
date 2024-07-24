'''
383. Ransom Note
Easy
Topics
Companies

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

 

Constraints:
    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNoteT = list(ransomNote.strip(" "))
        magazine = list(magazine.strip(" "))
        for index_l, letter in enumerate(ransomNote):
            if letter in magazine:
                magazine.pop(magazine.index(letter))
                ransomNoteT.pop(ransomNoteT.index(letter))
        return len(ransomNoteT) == 0
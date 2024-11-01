'''
3136. Valid Word
Solved
Easy
Topics
Companies
Hint

A word is considered valid if:
    It contains a minimum of 3 characters.
    It contains only digits (0-9), and English letters (uppercase and lowercase).
    It includes at least one vowel.
    It includes at least one consonant.

You are given a string word.
Return true if word is valid, otherwise, return false.

Notes:
    'a', 'e', 'i', 'o', 'u', and their uppercases are vowels.
    A consonant is an English letter that is not a vowel.


Example 1:
Input: word = "234Adas"
Output: true
Explanation:
This word satisfies the conditions.

Example 2:
Input: word = "b3"
Output: false
Explanation:
The length of this word is fewer than 3, and does not have a vowel.

Example 3:
Input: word = "a3$e"
Output: false
Explanation:
This word contains a '$' character and does not have a consonant.

Constraints:
    1 <= word.length <= 20
    word consists of English uppercase and lowercase letters, digits, '@', '#', and '$'.

'''



class Solution:
    def isValid(self, word: str) -> bool:
        word_summary = {
            "vowels": 0,
            "consonant": 0,
            "digits": 0
        }
        
        if len(word) >= 3:
            for char in word:
                char = char.lower()
                if char in ["@", "#", "$"]:
                    return False
                elif char in ["a", "e", "i", "o", "u"]:
                    word_summary["vowels"] +=1
                elif char in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                    word_summary["digits"] +=1
                else:
                    word_summary["consonant"] +=1
        else:
            return False

        return word_summary["vowels"] >=1 and word_summary["consonant"] >=1
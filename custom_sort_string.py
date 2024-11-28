'''
791. Custom Sort String
Solved
Medium
Topics
Companies

You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.
Return any permutation of s that satisfies this property.

 

Example 1:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c", "b", and "a".
Since "d" does not appear in order, it can be at any position in the returned string. "dcba", "cdba", "cbda" are also valid outputs.

Example 2:
Input: order = "bcafg", s = "abcd"
Output: "bcad"
Explanation: The characters "b", "c", and "a" from order dictate the order for the characters in s. The character "d" in s does not appear in order, so its position is flexible.
Following the order of appearance in order, "b", "c", and "a" from s should be arranged as "b", "c", "a". "d" can be placed at any position since it's not in order. The output "bcad" correctly follows this rule. Other arrangements like "dbca" or "bcda" would also be valid, as long as "b", "c", "a" maintain their order.

 

Constraints:
    1 <= order.length <= 26
    1 <= s.length <= 200
    order and s consist of lowercase English letters.
    All the characters of order are unique.


'''
# -------------------------------
# Import the alphabet
# -------------------------------
import string 


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # -------------------------------
        # Define the order based on the alphabet
        # -------------------------------
        alphabet = list(string.ascii_lowercase)
        priority = {}
        
        for idx, elem in enumerate(order):
            priority[elem] = idx
        
        remaining_priority = [elem for elem in alphabet if elem not in order]
        for elem in remaining_priority:
            priority[elem] = len(order) + alphabet.index(elem)
                
        # -------------------------------
        # Create a new dictionary with all the occurencies and elements of s
        # -------------------------------
        occurencies_count = {}
        for elem in s:
            occurencies_count[elem] = occurencies_count.get(elem, 0) + 1
            
        
        # -------------------------------
        # Iterate over the dictionary and sortit based on the priority
        # -------------------------------
        sorted_keys = sorted(occurencies_count.keys(), key = lambda x: priority[x])
        
        # -------------------------------
        # Create the result
        # -------------------------------
        result = ""
        for elem in sorted_keys:
            result +=  elem * occurencies_count[elem]
        return result
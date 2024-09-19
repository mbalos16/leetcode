'''
819. Most Common Word
Solved
Easy
Topics
Companies

Given a string paragraph and a string array of the banned words banned, return the most frequent word that is not banned. It is guaranteed there is at least one word that is not banned, and that the answer is unique.

The words in paragraph are case-insensitive and the answer should be returned in lowercase.

 

Example 1:

Input: paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]
Output: "ball"
Explanation: 
"hit" occurs 3 times, but it is a banned word.
"ball" occurs twice (and no other word does), so it is the most frequent non-banned word in the paragraph. 
Note that words in the paragraph are not case sensitive,
that punctuation is ignored (even if adjacent to words, such as "ball,"), 
and that "hit" isn't the answer even though it occurs more because it is banned.

Example 2:

Input: paragraph = "a.", banned = []
Output: "a"

 

Constraints:

    1 <= paragraph.length <= 1000
    paragraph consists of English letters, space ' ', or one of the symbols: "!?',;.".
    0 <= banned.length <= 100
    1 <= banned[i].length <= 10
    banned[i] consists of only lowercase English letters.


'''
class Solution:
    def __init__(self):
        self.new_dict = {}

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        str_list = paragraph.split(" ")
        
        for element in str_list:
            # check if the word has any of the symbols, if so eliminate them
            symbols = ["!", "?", "'", ",", ";", "."]
            element = element.lower()
            if element[len(element)-1:] in symbols:
                element = element[:-1]
            if "," in element:
                for char in element:
                    self.add_element(char)
            
            self.add_element(element)
        
        max_value = max(self.new_dict, key=self.new_dict.get)
        if len(banned) > 0:
            for element in banned:
                if element in self.new_dict:
                    del self.new_dict[element]
        return max(self.new_dict, key=self.new_dict.get)

    def add_element(self, element):
        if element in self.new_dict:
                self.new_dict[element] += 1
        else:
                self.new_dict[element] = 1
        
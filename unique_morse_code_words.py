'''
804. Unique Morse Code Words
Easy
Topics
Companies

International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

    'a' maps to ".-",
    'b' maps to "-...",
    'c' maps to "-.-.", and so on.

For convenience, the full table for the 26 letters of the English alphabet is given below:
[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.
    For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

 

Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

Example 2:
Input: words = ["a"]
Output: 1

 

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 12
    words[i] consists of lowercase English letters.
'''

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        dict_morse_letters = {
            "a" : ".-",
            "b" : "-...",
            "c" : "-.-.",
            "d" : "-..",
            "e" : ".",
            "f" : "..-.",
            "g" : "--.",
            "h" : "....",
            "i" : "..",
            "j" : ".---",
            "k" : "-.-",
            "l" : ".-..",
            "m" : "--",
            "n" : "-.",
            "o" : "---",
            "p" : ".--.",
            "q" : "--.-",
            "r" : ".-.",
            "s" : "...",
            "t" : "-",
            "u" : "..-",
            "v" : "...-",
            "w" : ".--",
            "x" : "-..-",
            "y" : "-.--",
            "z" : "--.."
        }
        morse_list = []
        for word in words:
            morse_word = ''
            for letter in word:
                if dict_morse_letters[letter.lower()]:
                    morse_word += dict_morse_letters[letter.lower()]
                else:
                    raise ValueError(print(f"Sorry, the letter {letter} was not found in the 26 English alphabet."))

            if morse_word not in morse_list:
                morse_list.append(morse_word)
        return len(morse_list)
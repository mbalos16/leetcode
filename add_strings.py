'''
415. Add Strings
Solved
Easy
Topics
Companies

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"

Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"

Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

 

Constraints:

    1 <= num1.length, num2.length <= 104
    num1 and num2 consist of only digits.
    num1 and num2 don't have any leading zeros except for the zero itself.


'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = self.get_int(num1)
        num2 = self.get_int(num2)
        return self.get_str(num1 + num2)
    
    def get_int(self, number):
        try:
            new_number = int(number)
        except ValueError:
            sys.set_int_max_str_digits(len(number))
            new_number = int( number)
        return new_number
    
    def get_str(self, number):
        try:
            new_number = str(number)
        except ValueError:
            sys.set_int_max_str_digits(8000)
            new_number = str( number)
        return new_number
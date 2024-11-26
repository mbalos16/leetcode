'''
1502. Can Make Arithmetic Progression From Sequence
Solved
Easy
Topics
Companies
Hint

A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

Example 1:
Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.

Example 2:
Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.


Constraints:
    2 <= arr.length <= 1000
    -106 <= arr[i] <= 106

'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        last_num = 0
        first_diff = 0
        for idx, elem in enumerate(sorted(arr)):
            if idx == 0:
                last_num = elem
            if idx == 1:
                first_diff = elem - last_num
                last_num = elem 
            else:
                diff_now = elem - last_num
                if diff_now != first_diff:
                    return False
                last_num = elem
        return True


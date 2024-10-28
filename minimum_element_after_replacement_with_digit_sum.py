'''
3300. Minimum Element After Replacement With Digit Sum
Solved
Easy
Topics
Hint
You are given an integer array nums.
You replace each element in nums with the sum of its digits.

Return the minimum element in nums after all replacements.

 

Example 1:
Input: nums = [10,12,13,14]
Output: 1
Explanation:
nums becomes [1, 3, 4, 5] after all replacements, with minimum element 1.

Example 2:
Input: nums = [1,2,3,4]
Output: 1
Explanation:
nums becomes [1, 2, 3, 4] after all replacements, with minimum element 1.

Example 3:
Input: nums = [999,19,199]
Output: 10

Explanation:
nums becomes [27, 10, 19] after all replacements, with minimum element 10.

Constraints:
    1 <= nums.length <= 100
    1 <= nums[i] <= 104


'''

class Solution:
    def minElement(self, nums: List[int]) -> int:
        seen_elem = {}
        list_of_digits = []
        for element in nums:
            if element not in seen_elem:
                digit_count = 0
                # sum any digit in the number 
                for digit in str(element):
                    digit_count +=int(digit)
                seen_elem[element] = digit_count
                
            # add the value of the number from the dictionary to the list 
            list_of_digits.append(seen_elem[element])
        return min(list_of_digits)
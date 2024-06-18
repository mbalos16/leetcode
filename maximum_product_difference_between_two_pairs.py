'''
1913. Maximum Product Difference Between Two Pairs

The product difference between two pairs (a, b) and (c, d) is defined as (a * b) - (c * d).
    For example, the product difference between (5, 6) and (2, 7) is (5 * 6) - (2 * 7) = 16.
Given an integer array nums, choose four distinct indices w, x, y, and z such that the product difference between pairs (nums[w], nums[x]) and (nums[y], nums[z]) is maximized.
Return the maximum such product difference.

Example 1:
Input: nums = [5,6,2,7,4]
Output: 34
Explanation: We can choose indices 1 and 3 for the first pair (6, 7) and indices 2 and 4 for the second pair (2, 4).
The product difference is (6 * 7) - (2 * 4) = 34.

Example 2:
Input: nums = [4,2,5,9,7,4,8]
Output: 64
Explanation: We can choose indices 3 and 6 for the first pair (9, 8) and indices 1 and 5 for the second pair (2, 4).
The product difference is (9 * 8) - (2 * 4) = 64.

Constraints:
    4 <= nums.length <= 104
    1 <= nums[i] <= 104

'''


# Option 1
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Get the two highest numbers
        max_num = max(nums)
        nums.remove(max(nums))
        max_num2 = max(nums)
        nums.remove(max(nums))

        # Get the two minimum numbers
        min_num = min(nums)
        nums.remove(min(nums))
        min_num2 = min(nums)
        nums.remove(min(nums))

        return (max_num * max_num2) - (min_num * min_num2)


# Option 2
class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        # Get the two highest numbers
        max_num, nums = max_min_number(nums, "max")
        max_num2, nums = max_min_number(nums, "max")

        # Get the two minimum numbers
        min_num, nums = max_min_number(nums, "min")
        min_num2, nums = max_min_number(nums, "min")
        return (max_num * max_num2) - (min_num * min_num2)


    def max_min_number(nums, operation):
        # Return the maximum number of a list and the list without that element
        if operation = "max":
            number = max(nums)
            nums = nums.remove(max(nums))
        elif operation = "min":
            number = min(nums)
            muns = nums.remove(min(nums))
        else:
            raise ValueError(f"Operation {operation} not found")
        return number, nums
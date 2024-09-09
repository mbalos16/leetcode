'''
349. Intersection of Two Arrays
Easy

Given two integer arrays nums1 and nums2, return an array of their
intersection
. Each element in the result must be unique and you may return the result in any order.

Example 1:
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

Constraints:
    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000
'''
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        new_list = []
        if len(nums1) > len(nums2):
            start = nums2
            compare = nums1
        else:
            start = nums1
            compare = nums2

        for number in start:
            if number in compare and number not in new_list:
                new_list.append(number)
        return new_list
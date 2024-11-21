'''
144. Binary Tree Preorder Traversal
Solved
Easy
Topics
Companies

Given the root of a binary tree, return the preorder traversal of its nodes' values.
 

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]
Explanation:

Example 2:
Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [1,2,4,5,6,7,3,8,9]
Explanation:

Example 3:
Input: root = []
Output: []

Example 4:
Input: root = [1]
Output: [1]

 

Constraints
    The number of nodes in the tree is in the range [0, 100].
    -100 <= Node.val <= 100

 

Follow up: Recursive solution is trivial, could you do it iteratively?
Seen this question in a real interview before?
1/5
Yes
No
Accepted
1.8M
Submissions
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            result = []
        else:
            stack = [root, ]
            result = []
            while stack:
                
                #Keep moving
                root = stack.pop()
    
                if root is not None:
                    # Add each visited node to the result
                    result.append(root.val)
                    # If there are childs of the actual root add them to the stack 
                    # These childs will be visited as new roots
                    if root.right is not None:
                        stack.append(root.right)
                    if root.left is not None:
                        stack.append(root.left)
        return result
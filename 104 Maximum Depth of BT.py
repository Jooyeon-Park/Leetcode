# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        return self.helper(root, 0)
    def helper(self, root, depth) -> int:
        left, right = 0,0
        if root.left:
            left = self.helper(root.left, depth)
        if root.right:
            right = self.helper(root.right, depth)
        return depth + 1 + max(left, right)
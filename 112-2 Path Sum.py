# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        return self.helper(root, 0, targetSum)
        
    def helper(self, root, sumSoFar, targetSum):
        sumSoFar += root.val
        print("SumSo Far!!: ", sumSoFar)
        print("TArget: ", targetSum)
        
        # Leaf node check
        if root.left is None and root.right is None:
            print("This is it!")
            return sumSoFar == targetSum
            
        # Initialize result to track if path exists in either subtree
        result = False
        
        if root.left:
            result = result or self.helper(root.left, sumSoFar, targetSum)
            
        if root.right:
            result = result or self.helper(root.right, sumSoFar, targetSum)
            
        return result

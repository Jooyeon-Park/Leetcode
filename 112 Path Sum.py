# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.helper(root)

    def helper(self, node):
        if node == None:
            return None

        if not node.left and not node.right:
            return node

        temp = node.left
        node.left = self.helper(node.right)
        node.right = self.helper(temp)

        return node

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # parse p tree into an array
        self.pList = []
        self.helper(p,self.pList)
        # parse q tree into an array
        self.qList = []
        self.helper(q, self.qList)
        # Compare arrays( )
        if self.pList == self.qList:
            return True
        else:
            return False

    def helper(self, node, arr):
        if node == None:
            return
        arr.append(node.val)
        if node.left == None:
            arr.append(None)
        else:
            self.helper(node.left, arr)
        
        if node.right == None:
            arr.append(None)
        else:
            self.helper(node.right,arr)

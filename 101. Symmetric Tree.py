# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        left, right = [], []
        self.helperL(left,root.left)
        self.helperR(right, root.right)
        # print(left,"\n", right)
        return left == right
    def helperL(self, arr, root):
        if root == None:
            arr.append(None)
            return
        else:
            arr.append(root.val)
        self.helperL(arr, root.left)
        self.helperL(arr, root.right)

    def helperR(self, arr, root):
        if root == None:
            arr.append(None)
            return
        else:
            arr.append(root.val)
        self.helperR(arr, root.right)
        self.helperR(arr, root.left)
    

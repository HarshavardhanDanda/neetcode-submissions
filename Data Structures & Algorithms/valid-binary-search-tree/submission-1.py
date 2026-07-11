# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        def valid(root, leftMargin, rightMargin):
            if root is None:
                return True
            if(root.val <= leftMargin or root.val >= rightMargin):
                return False
            return valid(root.left, leftMargin, root.val) and valid(root.right, root.val, rightMargin)
        return valid(root, float('-inf'), float('inf'))
        
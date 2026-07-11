# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isEqual(a, b):
            if(a is None and b is None):
                return True
            if(a is None or b is None):
                return False
            if(a.val != b.val):
                return False
            return isEqual(a.left, b.left) and isEqual(a.right, b.right)
        stack = [root]
        while(stack):
            k=stack.pop()
            if k is None:
                continue
            if isEqual(k, subRoot):
                return True
            stack.append(k.left)
            stack.append(k.right)
        return False






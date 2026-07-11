# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        d=deque([(p, q)])
        while(d):
            a,b = d.popleft()
            if a is None and b is None:
                continue
            if (a is None or b is None):
                return False
            if(a.val != b.val):
                return False
            d.append((a.left, b.left))
            d.append((a.right, b.right))
        return True
            









        
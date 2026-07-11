# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        output=[root.val]
        d=deque([root])
        while(d):
            right=None
            print([node.val for node in d])
            for i in range(len(d)):
                k=d.popleft()
                if(k.left):
                    d.append(k.left)
                if(k.right):
                    d.append(k.right)
            if(len(d)):
                output.append(d[-1].val)
        return output
            
            
            
        
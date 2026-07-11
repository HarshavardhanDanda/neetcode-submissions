# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root is None:
                return (0, True)

            leftHeight,leftBalanced=dfs(root.left)
            rightHeight,rightBalanced=dfs(root.right)

            height=1+max(leftHeight, rightHeight)
            balanced=leftBalanced and rightBalanced and (abs(rightHeight-leftHeight) <=1)
            
            return (height, balanced)
        return dfs(root)[1]
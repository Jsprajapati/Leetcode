"""

"""
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == root.left.val + root.right.val
        # print(root.val)
        # print(root.left.val)
        # print(root.right.val)
        # pass


s = Solution()
root = TreeNode(10)
root.left = TreeNode(4)
root.right = TreeNode(6)
print(s.checkTree(root))

s = Solution()
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(1)
print(s.checkTree(root))

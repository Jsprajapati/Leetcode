# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # sortedArray = []
        # stack = [root]

        # while len(stack) > 0:
        #     root = stack.pop()
        #     if root:

        #         stack.append(root.left)
        #         print(root.val)
        #         # sortedArray.append(root.val)
        #         stack.append(root.right)
        # print(sortedArray)
        ara = [[]]
        if root:
            ara = [[root.val]]

        def preorder(root):
            if root:
                l = root.left.val if root.left else None
                r = root.right.val if root.right else None
                ar = [l] if l else []
                print(ar)
                ar += r if r else ""

                # ar = [l, r]if l and r else []

                # if l or r:
                print(ar)
                ara.append([ar])
                preorder(root.left)
                print(root.val)
                preorder(root.right)
        preorder(root)
        print(ara)
        # return min(minDiff)


s = Solution()
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
root = TreeNode(3)
root.left = TreeNode(9)
root.left.left = TreeNode(1)
root.left.right = TreeNode(4)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

s.zigzagLevelOrder(TreeNode(None))

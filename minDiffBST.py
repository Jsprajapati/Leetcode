"""
783. Minimum Distance Between BST Nodes
Difficulty: Easy

Given the root of a Binary Search Tree (BST), return the minimum difference between the values
of any two different nodes in the tree.

Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1

Complexity Analysis:
Time: O(N)
Space: O(N)

Constraints:
The number of nodes in the tree is in the range [2, 100].
0 <= Node.val <= 105

Note: This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/
Date: 19-02-2023
Source: https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/
Solution: https://leetcode.com/problems/minimum-distance-between-bst-nodes/solutions/3070288/minimum-distance-between-bst-nodes/
"""
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        sortedArray = []

        def inOrder(root, val):
            if root:
                inOrder(root.left, root.val)
                sortedArray.append(root.val)
                inOrder(root.right, root.val)
        inOrder(root, root.val)
        minDiff = 999999
        for i in range(len(sortedArray)-1):
            diff = abs(sortedArray[i] - sortedArray[i+1])
            if minDiff > diff:
                minDiff = diff
        return minDiff


s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right = TreeNode(6)
print(s.minDiffInBSTItr(root))


# [1,0,48,null,null,12,49]
# Output: 1

root = TreeNode(1)
root.left = TreeNode(0)
root.right = TreeNode(48)
root.right.left = TreeNode(12)
root.right.right = TreeNode(49)
print(s.minDiffInBSTItr(root))


# [90,69,null,49,89,null,52]
root = TreeNode(90)
root.left = TreeNode(69)
# rnull
root.left.left = TreeNode(49)
root.left.right = TreeNode(89)
# null
root.left.left.right = TreeNode(52)

# print(s.minDiffInBSTItr(root))
print(s.minDiffInBSTItr(root))
"""


#  # def minDiffInBST(self, root: Optional[TreeNode]) -> int:
    #     minDiff = []

    #     def preorder(root, val):
    #         if root:
    #             preorder(root.left, root.val)
    #             if not root.val == val:
    #                 minDiff.append(abs(root.val - val))
    #             preorder(root.right, root.val)
    #     preorder(root, root.val)
    #     return min(minDiff)
    # Right Approach
            # return min(minDiff)
        # def preorder(root, val):
        #     if root:
        #         if not root.val == val:
        #             minDiff.append(abs(root.val - val))
        #         preorder(root.left, root.val)
        #         preorder(root.right, root.val)
        # preorder(root, root.val)
        # return min(minDiff)

    # def minDiffInBSTItr(self, root: Optional[TreeNode]) -> int:
    #     minDiff = root.val
    #     stack = [(root, root.val)]

    #     while len(stack) > 0:
    #         root, val = stack.pop()
    #         if root:
    #             stack.append((root.left, root.val))
    #             diff = abs(root.val - val)
    #             if minDiff > diff and diff != 0:
    #                 minDiff = diff

    #             stack.append((root.right, root.val))
    #     # print(minDiff)

    #     return minDiff
    def minDiffInBSTItr(self, root: Optional[TreeNode]) -> int:
        sortedArray = []
        stack = [root]

        while len(stack) > 0:
            root = stack.pop()
            if root:

                stack.append(root.left)
                sortedArray.append(root.val)
                stack.append(root.right)

        print(sortedArray)
        minDiff = 999999
        for i in range(len(sortedArray)-1):
            diff = abs(sortedArray[i] - sortedArray[i+1])
            if minDiff > diff:
                minDiff = diff
        return minDiff

        return sortedArray

"""

"""
938. Range Sum of BST
Difficulty: Easy

Given the root node of a binary search tree and two integers low and high, return the sum of values of all nodes with a
value in the inclusive range [low, high].

Example 1:
Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.

Example 2:
Input: root = [10,5,15,3,7,13,18,1,null,6], low = 6, high = 10
Output: 23
Explanation: Nodes 6, 7, and 10 are in the range [6, 10]. 6 + 7 + 10 = 23.


Constraints:
The number of nodes in the tree is in the range [1, 2 * 104].
1 <= Node.val <= 105
1 <= low <= high <= 105
All Node.val are unique

Complexity Analysis:
Time Complexity: O(N), where N is the number of nodes in the tree.
Space Complexity: O(N)

Date: 14-02-2023 23:40
Source: https://leetcode.com/problems/range-sum-of-bst/description/
Reference: https://leetcode.com/problems/range-sum-of-bst/solutions/192077/range-sum-of-bst/
"""

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    sum = 0

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def inorder(root):
            if root:
                inorder(root.left)
                print("Node", root.val)
                if root.val <= high and root.val >= low:
                    self.sum += root.val
                inorder(root.right)
        inorder(root)
        return self.sum

    def rangeSumBSTOptimisedRecursive(self, root: Optional[TreeNode], low: int, high: int) -> int:

        # Traverses only required nodes
        def dfs(node):
            if node:
                print("Node", node.val)
                if low <= node.val <= high:
                    self.sum += node.val
                if low <= node.val:
                    dfs(node.left)
                if node.val <= high:
                    dfs(node.right)
        dfs(root)
        return self.sum

    def rangeSumBSTOptimisedIterative(self, root: Optional[TreeNode], low: int, high: int) -> int:
        stack = [root]
        while stack:
            stk = [s.val for s in stack if s]
            print(stk)
            print("Stack ", stack)
            node = stack.pop()
            if node:
                print("Node", node.val)
                if low <= node.val <= high:
                    self.sum += node.val
                if low <= node.val:
                    stack.append(node.left)
                if node.val <= high:
                    stack.append(node.right)
        return self.sum


s = Solution()
#  [10,5,15,3,7,null,18], low = 7, high = 15
t = TreeNode(10)
t.left = TreeNode(5)
t.left.left = TreeNode(3)
t.left.right = TreeNode(7)
t.right = TreeNode(15)
t.right.left = None
t.right.right = TreeNode(18)

print(s.rangeSumBST(t, 7, 15))

s = Solution()
# [10, 5, 15, 3, 7, 13, 18, 1, null, 6], low = 6, high = 10
t = TreeNode(10)
t.left = TreeNode(5)
t.left.left = TreeNode(3)
t.left.left.left = TreeNode(1)
t.left.left.right = None
t.left.right = TreeNode(7)
t.right = TreeNode(15)
t.right.left = TreeNode(13)
t.right.left.left = TreeNode(6)
t.right.right = TreeNode(18)

print(s.rangeSumBST(t, 6, 10))

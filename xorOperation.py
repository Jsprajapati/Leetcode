"""
1486. XOR Operation in an Array
Easy
1.1K
308
Companies
You are given an integer n and an integer start.

Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.



Example 1:
Input: n = 5, start = 0
Output: 8
Explanation: Array nums is equal to [0, 2, 4, 6, 8] where (0 ^ 2 ^ 4 ^ 6 ^ 8) = 8.
Where "^" corresponds to bitwise XOR operator.

Example 2:
Input: n = 4, start = 3
Output: 8
Explanation: Array nums is equal to [3, 5, 7, 9] where (3 ^ 5 ^ 7 ^ 9) = 8.


Constraints:

1 <= n <= 1000
0 <= start <= 1000
n == nums.length

Complexity:
Time: O(n)
Space: O(1)

Source: https://leetcode.com/problems/xor-operation-in-an-array/description/
Solution: https://leetcode.com/problems/xor-operation-in-an-array/solutions/699141/visual-solution-python-o-1-time-o-1-space/?orderBy=most_votes
"""


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        # nums = [start+2*0]
        xorOp = start+2*0
        for i in range(1, n):
            ele = start + 2 * i
            xorOp ^= ele
            # nums.append(ele)
        return xorOp
        # print(nums)
        # print(xorOp)
        # for i in ran
        # pass


s = Solution()
n = 5
start = 0
print(s.xorOperation(n, start))
n = 4
start = 3
print(s.xorOperation(n, start))

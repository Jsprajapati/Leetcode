"""
2574. Left and Right Sum Differences
Easy
138
3
Companies
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
Return the array answer.



Example 1:
Input: nums = [10,4,8,3]
Output: [15,1,11,22]
Explanation: The array leftSum is [0,10,14,22] and the array rightSum is [15,11,3,0].
The array answer is [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

Example 2:
Input: nums = [1]
Output: [0]
Explanation: The array leftSum is [0] and the array rightSum is [0].
The array answer is [|0 - 0|] = [0].


Constraints:
1 <= nums.length <= 1000
1 <= nums[i] <= 105

Source: https://leetcode.com/problems/left-and-right-sum-differences/description/
Solution: https://leetcode.com/problems/left-and-right-sum-differences/solutions/3231177/simple-total-sum-partial-sum-o-n-time-o-1-space/

Complexity:
Time: n + n = 2n = o(n)
Space: 1 + n + n + n = 3n + 1 = O(n)
"""

from typing import List


class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        l = len(nums)
        lSum = [0] * l
        rSum = [0] * l
        for i in range(1, l):
            lSum[i] = lSum[i-1] + nums[i-1]
            rSum[l-i-1] = rSum[l-i] + nums[l-i]
        lrDiff = []
        for i in range(0, l):
            lrDiff.append(abs(lSum[i] - rSum[i]))
        return lrDiff


s = Solution()
nums = [10, 4, 8, 3]
print(s.leftRigthDifference(nums))
nums = [1]
print(s.leftRigthDifference(nums))

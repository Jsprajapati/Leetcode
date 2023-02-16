"""
1389. Create Target Array in the Given Order
Difficulty: Easy

Given two arrays of integers nums and index. Your task is to create target array under the following rules:
Initially target array is empty.
From left to right read nums[i] and index[i], insert at index index[i] the value nums[i] in target array.
Repeat the previous step until there are no elements to read in nums and index.
Return the target array.
It is guaranteed that the insertion operations will be valid.

Example 1:
Input: nums = [0,1,2,3,4], index = [0,1,2,2,1]
Output: [0,4,1,3,2]
Explanation:
nums       index     target
0            0        [0]
1            1        [0,1]
2            2        [0,1,2]
3            2        [0,1,3,2]
4            1        [0,4,1,3,2]

Example 2:
Input: nums = [1,2,3,4,0], index = [0,1,2,3,0]
Output: [0,1,2,3,4]
Explanation:
nums       index     target
1            0        [1]
2            1        [1,2]
3            2        [1,2,3]
4            3        [1,2,3,4]
0            0        [0,1,2,3,4]

Example 3:
Input: nums = [1], index = [0]
Output: [1]

Constraints:
1 <= nums.length, index.length <= 100
nums.length == index.length
0 <= nums[i] <= 100
0 <= index[i] <= i

Complexity Analysis:
Time: O(N)
Space: O(N)
Source:  https://leetcode.com/problems/create-target-array-in-the-given-order/description/
Best solution: https://leetcode.com/problems/create-target-array-in-the-given-order/solutions/1021340/python-using-insert-and-without-insert-very-easy/
Date: 16-02-2023
"""

from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        targetArray = []
        ind = 0
        for id in index:
            lst = len(targetArray)
            if lst < id:
                targetArray += [nums[id]]
            else:
                targetArray = targetArray[0:id] + \
                    [nums[ind]] + targetArray[id:lst]
            ind += 1
        return targetArray

    def createTargetArrayBest(self, nums: List[int], index: List[int]) -> List[int]:
        arr = []
        for n, i in zip(nums, index):
            arr.insert(i, n)
            # arr[i:i] = [n]
        return arr


s = Solution()
nums = [0, 1, 2, 3, 4]
index = [0, 1, 2, 2, 1]
print(s.createTargetArray(nums, index))

nums = [1, 2, 3, 4, 0]
index = [0, 1, 2, 3, 0]
print(s.createTargetArray(nums, index))

nums = [1]
index = [0]
print(s.createTargetArray(nums, index))

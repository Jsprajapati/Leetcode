"""
1313. Decompress Run-Length Encoded List
Difficulty: Easy

We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list.

Example 1:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]
Explanation: The first pair [1,2] means we have freq = 1 and val = 2 so we generate the array [2].
The second pair [3,4] means we have freq = 3 and val = 4 so we generate [4,4,4].
At the end the concatenation [2] + [4,4,4] is [2,4,4,4].

Example 2:
Input: nums = [1,1,2,3]
Output: [1,3,3]

Constraints:
2 <= nums.length <= 100
nums.length % 2 == 0
1 <= nums[i] <= 100

Complexity Analysis:
Time:
Space:

Source: https://leetcode.com/problems/decompress-run-length-encoded-list/
Date: 15-02-2023

"""
from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        possiblePairs = len(nums)/2
        decompressedList = []
        ind = 0
        while ind < possiblePairs:
            pair1 = [nums[2*ind], nums[2*ind+1]]
            decompressedList.extend(pair1[0]*[pair1[1]])
            ind += 1

        return decompressedList

    def decompressRLElistPro(self, A: List[int]) -> List[int]:
        return [x for a, b in zip(A[::2], A[1::2]) for x in [b] * a]


s = Solution()
# Input: nums = [1,1,2,3]
print(s.decompressRLElist([1, 2, 3, 4]))
print(s.decompressRLElist([1, 1, 2, 3]))
print(s.decompressRLElist([1, 'A', 2, 'B', 5, 'C']))

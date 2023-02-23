"""
1221. Split a String in Balanced Strings

Balanced strings are those that have an equal quantity of 'L' and 'R' characters.
Given a balanced string s, split it into some number of substrings such that:
Each substring is balanced.
Return the maximum number of balanced strings you can obtain.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLRRRLLRLL"
Output: 2
Explanation: s can be split into "RL", "RRRLLRLL", each substring contains same number of 'L' and 'R'.
Note that s cannot be split into "RL", "RR", "RL", "LR", "LL", because the 2nd and 5th substrings are not balanced.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".


Constraints:
2 <= s.length <= 1000
s[i] is either 'L' or 'R'.
s is a balanced string.

Source: https://leetcode.com/problems/split-a-string-in-balanced-strings/description/
Solution: https://leetcode.com/problems/split-a-string-in-balanced-strings/solutions/403836/c-java-python-easy-solution/?orderBy=most_votes

Complexity:
Time: O(n)
Space: O(1)
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = 0
        maxNoOfBalStr = 0
        for c in s:
            if c == "R":
                cnt += 1
            if c == "L":
                cnt -= 1
            if cnt == 0:
                maxNoOfBalStr += 1
        return maxNoOfBalStr


s = Solution()
st = "RLRRLLRLRL"
print(s.balancedStringSplit(st))
st = "RLRRRLLRLL"
print(s.balancedStringSplit(st))
st = "LLLLRRRR"
print(s.balancedStringSplit(st))

"""
989. Add to Array-Form of Integer
Easy
2.7K
229
Companies
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.



Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021


Constraints:

1 <= num.length <= 104
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 104


Complexity Analysis:
Time Complexity: O(max(N,logk))) where N is the length of A.
Space Complexity: O(max(N,logk))).

Source: https://leetcode.com/problems/add-to-array-form-of-integer/description/
Solution: https://leetcode.com/problems/add-to-array-form-of-integer/solutions/234456/add-to-array-form-of-integer/
"""
from typing import List


class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        n = num[0]
        for i in num[1:]:
            n = (n*10) + i
        finalNum = n + k
        le = len(str(finalNum))-1
        finalArr = []
        while le >= 0:
            div = 10**le
            s = int(finalNum / div)
            finalArr.append(s)
            finalNum = finalNum % div
            le -= 1
        return finalArr

    def addToArrayFormOpt(self, num: List[int], k: int) -> List[int]:
        num = int(''.join([str(elem) for elem in num])) + k
        res = [int(x) for x in str(num)]
        return res

    def addToArrayFormOff(self, A, K):
        A[-1] += K
        carry = 0
        for i in range(len(A) - 1, -1, -1):
            print(i)
            carry, A[i] = divmod(A[i], 10)
            print(carry)
            if i:
                A[i-1] += carry
        if carry:
            print("VA", carry)
            A = list(map(int, str(carry))) + A
        return A


s = Solution()
print(s.addToArrayFormOff([1, 2, 0, 0], 34))
print(s.addToArrayFormOff([2, 7, 4], 181))
print(s.addToArrayFormOff([2, 1, 5], 806))

import math
from typing import List


class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        eleSum = 0
        digiSum = 0
        for ele in nums:
            eleSum += ele
            while ele != 0:
                digiSum += ele % 10
                ele = math.floor(ele / 10)
        print(eleSum)
        print(digiSum)
        return int(math.fabs(eleSum - digiSum))


print(Solution().differenceOfSum([1, 15, 6, 3]))

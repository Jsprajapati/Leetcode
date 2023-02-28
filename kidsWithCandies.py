from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        candiesBool = []
        maxCandies = 0
        for candy in candies:
            if maxCandies < candy:
                maxCandies = candy
        
        for kidCandies in candies:
            if kidCandies + extraCandies >= maxCandies:
                candiesBool.append(True)
            else:
                candiesBool.append(False)
        print(candiesBool)
        return candiesBool
    
# Solution.kidsWithCandies(list([2,3,5,1,3]),3)
S = Solution()
S.kidsWithCandies([2,3,5,1,3],3)
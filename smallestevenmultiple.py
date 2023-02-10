class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 == 0:
            return n
        else:
            return n*2 


s = Solution()
print(s.smallestEvenMultiple(5))
print(s.smallestEvenMultiple(6))
print(s.smallestEvenMultiple(12))
print(s.smallestEvenMultiple(15))

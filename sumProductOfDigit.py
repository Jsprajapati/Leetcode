import operator
from functools import reduce


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumOfDigits = 0
        productOfDigits = 1
        while n!= 0:
            digit = n % 10
            n = int(n / 10)
            print(digit)
            sumOfDigits += digit
            productOfDigits *= digit
            # print(productOfDigits)
        
        print(sumOfDigits)            
        print(productOfDigits)

        return productOfDigits - sumOfDigits

    def subtractProductAndSum2(self, n):
        A = map(int, str(n))
        print(A)
        x = reduce(operator.mul, A) 
        print(A)
        y = reduce(sum,A)
        print(x,y)
        return x-y
s = Solution()
import time

# start = time.time()
# print(s.subtractProductAndSum(234))
# end = time.time()
# print(end - start)

start2 = time.time()
print(s.subtractProductAndSum2(234))
end2 = time.time()
print(end2 - start2)

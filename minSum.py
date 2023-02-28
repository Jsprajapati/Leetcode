class Solution:
    def minimumSum(self, num: int) -> int:
        digits = sorted(list(str(num)))
        return int(digits[0]+digits[2]) + int(digits[1]+digits[3]) 

print(Solution().minimumSum(2392))
print(Solution().minimumSum(4009))

# 0123


# def sort(digits):/
    # sorted_t.append(digits[0])
    # for i in range(1,len(digits)):
        # if digits[i] in sorted_t:
        # print(i)


# sort([2,3,9,2])

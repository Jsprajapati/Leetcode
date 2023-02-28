from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # bin search
        low = 0
        high = len(nums) - 1
        # print("h", high)
        # print("t", target)
        # if target > nums[high-1]:
        #     return high
        itr = 0
        while low <= high:
            # itr += 1
            # print("Itr", itr)
            # if nums[low] > target and nums[high] < target:
            mid = (low + high) // 2
            # print(mid)
            if nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                # print("Else")
                return mid
            #     print(f"Found at {mid} -> {nums[mid]}")
            #     # print("itr", itr)
            #     return mid
            # low += 1
        return low
        # print("low", low)
        # print("mid", mid)
        # print("high", high)
        # if nums[mid] > target:
        #     return mid + 1
        # elif nums[mid] < target:
        #     return mid
        # pass


s = Solution()
# nums = [1, 3, 5, 6]
# target = 5
# print(s.searchInsert(nums, target))
# # Output: 2


nums = [1, 3, 5, 6]
target = 2
print(s.searchInsert(nums, target))
# # Output: 1


nums = [1, 3, 5, 6]
target = 7
print(s.searchInsert(nums, target))
# Output: 4


nums = [1, 3, 5, 6, 8, 9, 20, 28, 35, 37, 46, 52, 56, 67, 88, 90, 103, 123]
target = 20
print(s.searchInsert(nums, target))

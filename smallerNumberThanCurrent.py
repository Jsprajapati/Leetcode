from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        retArray = []
        for n in range(0,len(nums)):
            cnt = 0
            for m in range(0,len(nums)):
                if nums[n] > nums[m]:
                    cnt += 1
            retArray.append(cnt)
        # print(retArray)

s = Solution()
s.smallerNumbersThanCurrent([6,5,4,8])
s.smallerNumbersThanCurrent([7,7,7,7])
s.smallerNumbersThanCurrent([8,1,2,2,3])

# class Solution2:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         count={}
#         for i,v in enumerate(sorted(nums)):
#             if(v not in count):
#                 count[v]=i;
#         return [count[k] for k in nums];

# s = Solution2()
# print(s.smallerNumbersThanCurrent([6,5,4,8]))
# print(s.smallerNumbersThanCurrent([7,7,7,7]))
# print(s.smallerNumbersThanCurrent([8,1,2,2,3]))
class Solution3:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sortedNums=sorted(nums)
        print(sortedNums)
        currentNo=None
        smallerNo=0
        counter={}
        for num in sortedNums:
            print(num)
            if num!=currentNo:
                print("If")
                counter[num]=smallerNo
                currentNo=num
            print(counter[num])
            smallerNo+=1
        print(counter)
        return [counter[x] for x in nums]

s = Solution3()
# print(s.smallerNumbersThanCurrent([6,5,4,8]))
print(s.smallerNumbersThanCurrent([7,7,8,7]))
# print(s.smallerNumbersThanCurrent([8,1,2,2,3]))


# min = 1
# max = 8


# min = 0
# max = 99







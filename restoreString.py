from typing import List


class Solution:
    # def restoreString(self, s: str, indices: List[int]) -> str:
    #     out = ""
    #     d = dict(zip(indices, s))
    #     for i in range(len(d)):
    #         out += d[i]
    #     return out
    # def restoreString(self, s: str, indices: List[int]) -> str:
    #     res = [''] * len(s)
    #     for index, char in enumerate(s):
    #         res[indices[index]] = char
    #     return "".join(res)
    def restoreString(self, s: str, indices: List[int]) -> str:
        x = ""
        for index, char in enumerate(indices):
            # t = s[index]
            x += s[indices[index]]
            # s[char] = t
        print(x)

        # pass


st = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
s = Solution()
print(s.restoreString(st, indices))
st = "abc"
indices = [0, 1, 2]
print(s.restoreString(st, indices))

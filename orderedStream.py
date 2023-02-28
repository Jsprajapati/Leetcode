from typing import List


class OrderedStream:

    ar = []
    ptr = 0

    def __init__(self, n: int):
        self.ar = [None]*(n+1)

    def insert(self, idKey: int, value: str) -> List[str]:
        self.ar[idKey-1] = value
        oldptr = self.ptr
        print(self.ptr)
        # print(oldptr)
        cnt = 0
        for l in range(self.ptr, len(self.ar)):
            cnt += 1
            if not self.ar[l]:
                self.ptr = l
                break
        # for ind, val in enumerate(self.ar):
        #     cnt += 1
        #     if not val:
        #         self.ptr = ind
        #         break
            # if not val:
            #     self.ptr = ind
            #     break
        # print(self.ptr)
        print("Loop Count", cnt)
        return self.ar[oldptr:self.ptr]

        # if self.ar[idKey] != None:

        # Your OrderedStream object will be instantiated and called as such:
        # obj = OrderedStream(n)
        # param_1 = obj.insert(idKey,value)
n = 5
os = OrderedStream(n)
print(os.insert(3, "ccccc"))  # // Inserts (3, "ccccc"), returns [].
print(os.insert(2, "bbbbb"))
print(os.insert(1, "aaaaa"))  # // Inserts (1, "aaaaa"), returns ["aaaaa"].
# // Inserts (2, "bbbbb"), returns ["bbbbb", "ccccc"].
print(os.insert(5, "eeeee"))  # // Inserts (5, "eeeee"), returns [].
print(os.insert(4, "ddddd"))  # /
# [[5], [3, "ccccc"], [1, "aaaaa"], [2, "bbbbb"], [5, "eeeee"], [4, "ddddd"]]

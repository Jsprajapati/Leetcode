from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        start, end = s.split(":")
        startCol = ord(start[:1])
        startRow = int(start[1:])
        endCol = ord(end[:1])
        endRow = int(end[1:])
        li = []
        for col in range(startCol, endCol+1):
            # print("col", col)
            for row in range(startRow, endRow+1):
                # print("row", row)
                li.append(f"{chr(col)}{row}")

        return (li)
    # for startCol <= endCol:


s = Solution()
st = "K1:L2"
s.cellsInRange(st)
st = "A1:F2"
s.cellsInRange(st)

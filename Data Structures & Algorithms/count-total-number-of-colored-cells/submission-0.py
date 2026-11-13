class Solution:
    def coloredCells(self, n: int) -> int:
        s = 1
        for i in range(1, n):
            s += 4*i
        return s


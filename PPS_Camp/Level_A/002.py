# https://leetcode.com/problems/pascals-triangle/
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        L = []
        L.append([1])
        if numRows == 1:
            return L
        elif numRows == 2:
            L.append([1, 1])
            return L
        else:
            L.append([1, 1])
            temp = 0

            for i in range(2, numRows):
                L.append([])
                L[i].append(1)

                for j in range(1, i):
                    temp = L[i - 1][j - 1] + L[i - 1][j]
                    L[i].append(temp)

                L[i].append(1)
            return L
# Sqrt(x)
# https://leetcode.com/problems/sqrtx/submissions/

class Solution:
    def mySqrt(self, x: int) -> int:
        temp = pow(x, (1.0 / 2.0))

        temp = int(temp)

        return temp
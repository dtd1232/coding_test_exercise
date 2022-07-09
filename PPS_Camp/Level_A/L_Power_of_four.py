# Power of four
# https://leetcode.com/problems/power-of-four/submissions/

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        i = 0
        if n <= 0:
            return False
        else:
            while n % 4 == 0:
                n /= 4
            if n == 1:
                return True
            else:
                return False

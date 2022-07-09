# Valid Perfect Square
# https://leetcode.com/problems/valid-perfect-square/submissions/

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if pow(num, 1.0/2.0) % 1 == 0:
            return True
        else:
            return False
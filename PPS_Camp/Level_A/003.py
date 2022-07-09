# Plus One
# https://leetcode.com/problems/plus-one/submissions/

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        nums = int(''.join(digits))
        nums += 1
        nums = list(str(nums))
        nums = list(map(int, nums))

        return nums
# https://leetcode.com/problems/reverse-prefix-of-word/

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        cnt = 0

        if ch not in word:
            return word

        for i in word:
            if i != ch:
                cnt += 1
            elif i == ch:
                reverse_str = word[cnt::-1] + word[cnt + 1:]
                return reverse_str
            else:
                return word
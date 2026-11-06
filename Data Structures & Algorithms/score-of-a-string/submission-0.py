class Solution:
    def scoreOfString(self, s: str) -> int:
        i = 1
        sum = 0
        while i < len(s):
            sum += abs(ord(s[i]) - ord(s[i-1]))
            i += 1
        return sum
        
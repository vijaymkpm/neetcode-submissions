class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charMap = {}
        start = 0
        maxLength = 0

        for end, char in enumerate(s):

            if char in charMap and charMap[char] >= start:
                start = charMap[char] + 1

            charMap[char] = end

            maxLength = max(maxLength, end - start + 1)
        
        return maxLength
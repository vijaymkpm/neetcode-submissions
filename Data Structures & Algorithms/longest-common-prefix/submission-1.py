class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs:
            return res
        base = strs[0]

        for i, ch in enumerate(base):
            for word in strs[1:]:
                if i == len(word) or word[i] != ch:
                    return base[:i]
        return base
        
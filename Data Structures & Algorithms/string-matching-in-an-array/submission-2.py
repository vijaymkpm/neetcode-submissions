class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=len)
        i = 0
        res = []
        for i in range(len(words)):
            current = words[i]
            for j in range(i+1, len(words)):
                if current in words[j]:
                    res.append(current)
                    break
        return res
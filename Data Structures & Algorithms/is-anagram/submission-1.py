class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        if len(s) != len(t):
            return False
        map = {}
        for ch in s:
            if ch in map: 
                map[ch] += 1
            else:
                map[ch] = 1
        
        for ch in t:
            if ch in map:
                if map[ch] == 1:
                    del map[ch]
                else:
                    map[ch] -=1 
            else:
                return False
        
        if len(map.keys()) > 0:
            return False
        
        return True
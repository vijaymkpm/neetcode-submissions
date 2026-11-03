class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {'}':'{', ']':'[', ')':'('}

        for x in s:
            if x in map.values():
                stack.append(x)
            elif x in map:
                if not stack or stack.pop() != map[x]:
                    return False
        
        return len(stack) == 0
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        map = {'}':'{', ']':'[', ')':'('}

        for ch in s:
            if ch in map.keys():
                if len(stack) != 0:
                    last = stack.pop()
                    if last != map[ch]:
                        return False
                else:
                    return False
            else:
                stack.append(ch)

        return len(stack) == 0
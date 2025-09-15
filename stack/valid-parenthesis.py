class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        if s[0] in map:
            return False

        for i in range(len(s)):
            value = s[i]
            if value not in map:
                stack.append(value)
            elif len(stack) > 0 and map[value] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0
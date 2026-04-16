class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in range(len(s)):
            char = s[i]
            if char in "({[":
                stack.append(char)
           
            else:
                if not stack:
                    return False
                top = stack.pop()
                if char == ")" and top != "(":
                    return False
                if char == "}" and top != "{":
                    return False
                if char == "]" and top != "[":
                    return False
        
        return len(stack) == 0

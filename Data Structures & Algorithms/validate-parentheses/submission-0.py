class Solution:
    def isValid(self, s: str) -> bool:
        
        closeit = {
        ")": "(",
        "}": "{",
        "]": "["
        }

        stack = []

        for bracket in s:
            if bracket in closeit:
                if not stack:
                    return False
                top = stack.pop()
                if closeit[bracket] != top:
                    return False
            else:
                stack.append(bracket)

        if stack: 
            return False
        else:
            return True
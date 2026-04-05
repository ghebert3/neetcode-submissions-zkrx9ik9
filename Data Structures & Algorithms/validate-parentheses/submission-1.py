class Solution:
    def isValid(self, s: str) -> bool:
    

        paraclose = {
            ")" :  "(",
            "}" :  "{",
            "]" :  "["
        }

        stack  =[]

        for bracket in s:
            if bracket in paraclose:
                if not stack:
                    return False
                top = stack.pop()

                if paraclose[bracket] != top:
                    return False
            else:
                stack.append(bracket)

        if stack:
            return False
        else:
            return True
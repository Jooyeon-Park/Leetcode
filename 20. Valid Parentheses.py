class Solution:
    def isValid(self, s: str) -> bool:
        openBracket = ['(', '{', '[']
        closeBracket = [')', '}', ']']
        stack = []

        for i in s:
            if i in openBracket:
                stack.append(i)
            else:
                if len(stack) > 0 and closeBracket[openBracket.index(stack[-1])] == i:
                    stack.pop()
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False

        
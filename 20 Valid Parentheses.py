class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ['(', '[', '{']
        closing = [')',']','}']

        for char in s:
            if char in opening:
                stack.append(char)
            
            if char in closing:
                if len(stack) == 0:
                    return False
                if opening.index(stack[-1]) == closing.index(char):
                    stack.pop()
                else:
                    return False

        # Checking if the stack is empty
        if len(stack) != 0:
            return False
        else:
            return True
        
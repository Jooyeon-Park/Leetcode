class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        output = 0
        for i in tokens:
            if i == "+":
                num = stack.pop() + stack.pop()
                stack.append(num)
            elif i == "-":
                b = stack.pop()
                a = stack.pop()
                stack.append(a - b)
            elif i == "*":
                num = stack.pop() * stack.pop()
                stack.append(num)
            elif i == "/":
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(i))
        return stack.pop()
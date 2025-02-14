class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_a = int(a)
        int_b = int(b)
        sum = int_a + int_b
        if sum == 0:
            return "0"

        up = 0
        digit = 0
        output = ""

        while sum > 0:
            # print("Sum: ", sum)
            if sum % 10 + up >= 2:
                output += str(sum % 10 + up -2)
                up = 1
            else:
                output += str((sum % 10) + up)
                up = 0
            sum = sum // 10
        if up == 1:
            output += "1"
        return output[::-1]



class Solution:
    def hammingWeight(self, n: int) -> int:
        digit = 31
        output = 0

        while n > 0 and digit >= 0:
            if n >= 2 ** digit:
                n -= 2 ** digit
                output += 1
            digit -= 1
        return output
class Solution:
    def romanToInt(self, s: str) -> int:
        i = 0
        sum = 0
        symbol = 0
        rev = reversed(s)
        s = list(rev)
        symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        while i < len(s):
            if symbols[s[i]] < symbol:
                sum -= symbols[s[i]]
            else:
                sum += symbols[s[i]]
                symbol = symbols[s[i]]
            i += 1
        return sum
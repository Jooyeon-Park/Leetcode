class Solution:
    def intToRoman(self, num: int) -> str:
        output = ""
        digitRead = 1
        symbols = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        length = len(str(num))
        while digitRead <= length:
            digit = num % 10
            if digit == 4:
                output += symbols[5 * 10 ** (digitRead -1)] + symbols[1 * 10 ** (digitRead -1)]
            elif digit == 9:
                output += symbols[1 * 10 ** digitRead] + symbols[1 * 10 ** (digitRead -1)]
            else:
                if digit >= 5:                
                    temp = symbols[5 * 10 ** (digitRead-1)]
                    digit -= 5
                    temp += digit * symbols[10 ** (digitRead -1)]
                    output += temp[::-1]
                else:
                    output += digit * symbols[10 ** (digitRead -1)]
            num = num // 10
            digitRead += 1

        return output[::-1]
    

    # Hoon's solution here: I like it.
    # roman_map = [
    #         (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
    #         (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
    #         (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    #     ] 
    #     roman_numeral = ""
    #     for value, symbol in roman_map:
    #         count = num // value
    #         roman_numeral += symbol * count
    #         num %= value

    #     return roman_numeral
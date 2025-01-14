class Solution:
    def reverseWords(self, s: str) -> str:
        splited = s.split()
        output = ""

        for i in splited[::-1]:
            output += i + " "
        return output[:-1]
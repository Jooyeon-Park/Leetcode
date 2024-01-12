class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = False
        count = 0
        for i in range(len(s)-1,-1,-1):
            print(i)
            if string:
                if not s[i].isalpha():
                        return count
                count += 1
            else:
                if s[i].isalpha():
                    string = True
                    count += 1
        return count
        
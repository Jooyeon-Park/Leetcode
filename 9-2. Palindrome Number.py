class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        i = 0
        string = str(x)
        while i < len(string)//2:
            if string[i] != string[-1-i]:
                return False
            i += 1

        return True
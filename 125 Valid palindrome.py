class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for i in s:
            if i.isalnum():
                newString += i.lower()
        i = 0
        while i < len(newString) // 2:
            if newString[i] != newString[-1-i]:
                return False
            i += 1
        
        return True
            
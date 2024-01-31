class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: 
            return False
        elif x < 10:
            return True

        start = 0
        end = len(str(x))-1
        while start < end:
            if (x//10**start)%10 != (x//10**end)%10:
                return False
            start += 1
            end -= 1
        return True
            
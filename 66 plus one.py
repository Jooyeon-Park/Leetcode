class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        i = len(digits)-1
        isRunning = False

        digits[i] += 1
        if digits[i] == 10:
            isRunning = True
            digits[i] = 0
        i -= 1
        
        while i >= 0:
            if isRunning:
                if digits[i] + 1 == 10:
                    isRunning = True
                    digits[i] = 0
                else:
                    digits[i] += 1
                    isRunning = False
            i -= 1
        if isRunning:
            digits = [1] + digits
        return digits

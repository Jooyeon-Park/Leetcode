class Solution:
    def isHappy(self, n: int) -> bool:
        dictionary = {}
        while True:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit ** 2
                n = n//10    
            # print(sum)

            if sum in dictionary:
                return False
            if sum == 1:
                return True
            dictionary[sum] = 1
            n = sum    
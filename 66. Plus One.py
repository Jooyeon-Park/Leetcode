class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        sum = 0
        for i in digits[::-1]:
            sum += i * 10 ** num
            num += 1
        
        sum += 1

        i = 0
        output = []
        while sum > 0:
            output.append(sum%10)
            sum = sum//10

        return output[::-1]
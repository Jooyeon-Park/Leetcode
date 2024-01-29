class Solution:
    def helper(self, n: int, visited: set) -> bool:
        if n == 1:
            return True
        if n in visited:
            return False
        visited.add(n)
        
        new_n = 0
        while n > 0:
            digit = n % 10
            new_n += digit * digit
            n //= 10
        
        return self.helper(new_n, visited)

    def isHappy(self, n: int) -> bool:
        visited = set()
        return self.helper(n, visited)


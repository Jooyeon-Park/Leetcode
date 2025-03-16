class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        self.sum = None
        self.helper(triangle, 0)
        return self.sum

    def helper(self, triangle: List[List[int]], i):
        self.sum += 

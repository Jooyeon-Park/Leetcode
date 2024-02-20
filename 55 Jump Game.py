class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxI = 0
        if len(nums) == 1:
            return True

        for i, num in enumerate(nums):
            if i > maxI:
                return False
            if i + num >= len(nums)-1:
                return True
            maxI = max(maxI, i+num)
        
        return False

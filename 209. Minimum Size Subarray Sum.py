class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        left, right = 0, 0
        minLength = len(nums)
        total = 0
        for right in range(len(nums)):
            total += nums[right]
            while total >= target:
                minLength = min(minLength, right - left + 1)
                total -= nums[left]
                left += 1
            right += 1
        return minLength

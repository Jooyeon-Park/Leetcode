class Solution(object):
    def rotate(self, nums, k):
        if len(nums) == 0:
            return []
        k = k%len(nums)
        if k == 0:
            return nums
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])
        return nums
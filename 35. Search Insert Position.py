class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            num = self.helper(nums, target)
            if num > target:
                return nums.index(num)
            else:
                return nums.index(num) + 1

    def helper(self, nums:List[int], target):
        print(nums)
        if len(nums) == 1:
            return nums[0]

        if nums[len(nums)//2] < target:
            return self.helper(nums[len(nums)//2:], target)
        else:
            return self.helper(nums[:len(nums)//2], target)
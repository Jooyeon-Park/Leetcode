class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        # index = len(nums) - k
        newArr = nums[(len(nums)-k):] + nums[:(len(nums)-k)]
        # print(newArr)
        for i in range(0, len(nums)):
            nums[i] = newArr[i]
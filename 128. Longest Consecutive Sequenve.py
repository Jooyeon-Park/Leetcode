class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums = list(set(nums))
        nums.sort()
        # print(nums)
        maxLength = 1
        length = 1
        prev = nums[0]
        for i in range(1,len(nums)):
            # print("Prev: ", prev)
            if nums[i] == prev + 1:
                length += 1
                maxLength = max(maxLength, length)
            else:
                length = 1

            prev = nums[i]
            
        return maxLength
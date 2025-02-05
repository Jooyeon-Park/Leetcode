class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        
        jumps, furthest, jump_end = 0,0,0

        for i in range(len(nums)-1):
            furthest = max(furthest, nums[i] + i)

            if i == jump_end:
                jump_end = furthest
                jumps += 1

                if jump_end >= len(nums) - 1:
                    break
        return jumps
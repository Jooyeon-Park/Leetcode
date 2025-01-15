class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps, max_reach, steps = 0, 0, 0

        for i in range(len(nums)-1):
            max_reach = max(max_reach, i + nums[i])
            if i == steps:
                jumps += 1
                steps = max_reach
        return jumps
    
    # I don't get it though
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        i = 0
        start = -1 #If -1 -> wasn't continuing

        while i < len(nums):
            if i == len(nums)-1:
                if start == -1:
                    output.append(str(nums[i]))
                else:
                    output.append(str(start) + "->" + str(nums[i]))
                    start = -1
                break

            if nums[i + 1] == nums[i] + 1: #continuous
                if start == -1:
                    start = nums[i]
            else: # Not continuous
                if start == -1:
                    output.append(str(nums[i]))
                else:
                    output.append(str(start) + "->" + str(nums[i]))
                    start = -1
            i += 1
        return output

        
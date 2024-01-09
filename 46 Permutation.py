class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        #Helper
        def helper(nums, per=[], result=[]):
            if not nums:
                result.append(per[::])
                return result
            
            for i in range(0,len(nums)):
                newNums = nums[:i] + nums[i+1:]
                per.append(nums[i])
                helper(newNums,per,result)
                per.pop()
            return result
            

        return helper(nums)

        
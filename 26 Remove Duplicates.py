class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appeared = {}
        i=0
        while i < len(nums):
            if nums[i] in appeared.keys():
                return True
            else:
                appeared[nums[i]] = True
                i += 1
        return False
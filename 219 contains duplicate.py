class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:   
        for i in range(0,len(nums)):
            if nums[i] in nums[i+1:min(i+1+k, len(nums))]:
                return True
        return False       
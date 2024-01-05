class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0

        start,end = 0, len(nums)-1
        while start <= end: #O(n)
            if nums[end] == val:
                end -= 1

            elif nums[start] == val:
                nums[start] = nums[end]
                end -= 1
                start += 1

            else:
                start += 1

            
        return end + 1
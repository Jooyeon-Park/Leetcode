class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        k = 0  # pointer for placing the next unique element
        for i in range(1, len(nums)):
            if nums[i] != nums[k]:  # if a new unique element is found
                k += 1
                nums[k] = nums[i]  # move it to the next position in the array

        return k + 1
# January 3 
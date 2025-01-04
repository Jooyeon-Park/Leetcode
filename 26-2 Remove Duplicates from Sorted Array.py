class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dupe = set()
        index = 0

        for i in range(0, len(nums)):
            if nums[i] in dupe:
                continue
            else:
                dupe.add(nums[i])
                nums[index] = nums[i]
                index += 1
        return index    
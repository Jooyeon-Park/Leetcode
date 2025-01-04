class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            if nums[end] == val:
                end -= 1
                continue

            if nums[start] == val:
                temp = nums[start]
                nums[start] = nums[end]
                nums[end] = nums[start]

                start += 1
                end -= 1
                continue
            else:
                start += 1
        
        return start




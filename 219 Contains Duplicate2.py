class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {} # key: value // value: index of the number
        for i, value in enumerate(nums):
            if value in d and abs(i - d[value]) <= k:
                return True
            else:
                d[value] = i
        return False
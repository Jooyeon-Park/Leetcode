class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        dic = {}
        i = 0
        result = 0
        while i < len(nums):
            if nums[i] in dic.keys():
                if dic[nums[i]] == 2:
                    # nums.append(nums[i])
                    nums.pop(i)
                else:
                    dic[nums[i]] += 1 
                    result += 1
                    i += 1           
            else:
                dic[nums[i]] = 1
                result += 1
                i += 1
        return result

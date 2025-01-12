class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for i in nums:
            print("Current Gas: ", gas)
            if gas < 0:
                return False
            if i > gas:
                gas = i
            gas -= 1
        return True
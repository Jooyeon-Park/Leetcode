def summaryRanges(self, nums: List[int]) -> List[str]:
    if not nums:
        return []
    
    output = []
    s, e = nums[0], nums[0]
    
    for i in range(1, len(nums)):
        if e + 1 == nums[i]:
            e = nums[i]
        else:
            # Add the current range
            output.append(f"{s}->{e}" if s != e else f"{s}")
            s = nums[i]
            e = nums[i]
    
    # Don't forget to add the last range
    output.append(f"{s}->{e}" if s != e else f"{s}")
    
    return output
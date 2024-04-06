def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    # use sliding window algorithm and shift r in 
    # every loop to the right while doing 
    # this add up the element at posistion [right]
    # to a variable total 
    #  once that is done whenver
    # total greater than target shift left to the 
    # right to find minimum length
    left,total = 0,0
    res = len(nums) +1
    for r in range(len(nums)):
        total+=nums[r]
        while total >= target:
            res = min(r-left+1,res)
            total-=nums[left]
            left += 1
    print(res)
    if res > len(nums):
        return 0
    else:
        return res

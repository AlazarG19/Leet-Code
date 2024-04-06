def minSubArrayLen(self, target: int, nums: List[int]) -> int:
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

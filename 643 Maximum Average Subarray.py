def findMaxAverage(self, nums: List[int], k: int) -> float:
    maxavg = sum([nums[x] for x in range(k)])
    start = 0
    end = k
    prevavg = maxavg
    while(len(nums) > end):
        prevavg = prevavg+nums[end]-nums[start]
        maxavg = max(prevavg,maxavg)
        start+=1
        end+=1
    return maxavg/k


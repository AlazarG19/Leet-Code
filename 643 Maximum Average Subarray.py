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

# solution created using from using sliding window algorithm where
# instead of creating a subarrray of k elements and calculating the final
# average add the first k elements and find the highest sum
# by removing the first element and adding the last element
# and then finally dividing by k
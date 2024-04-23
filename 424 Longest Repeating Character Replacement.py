# use sliding window to check the frequency of characters. 
# when k < minimum frequency shift the left so that 
# k> minimum frequency . THe sum is the difference between 
# the left and right

def characterReplacement(self, s: str, k: int) -> int:
    l = 0
    count = {}
    res = 0
    for r in range(len(s)):
        count[s[r]] = count.get(s[r],0) +1
        while (r-l+1)-max(count.values()) > k:
            count[s[l]] = count.get(s[l]) - 1
            l +=1
        res = max(res,r-l+1)
    return res

                
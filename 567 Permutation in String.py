# use sliding window function and store all the characters
# inside hashes store each characters
def checkInclusion(self, s1: str, s2: str) -> bool:
    start = 0 
    end = len(s1)
    isperm = False
    hash1 = {}
    hash2 = {}
    if len(s1) > len(s2):
        return False
    for i in range(len(s1)):
        hash1[s1[i]] = hash1.get(s1[i],0) +1
        hash2[s2[i]] = hash2.get(s2[i],0) +1
    if hash2 == hash1 :
        isperm = True
    else:
        while end < len(s2):
            if(hash2[s2[start]] == 1):
                del hash2[s2[start]]
            else:
                hash2[s2[start]] -= 1
            hash2[s2[end]] = hash2.get(s2[end],0) +1
            print(hash1,hash2)
            if hash2 == hash1:
                isperm = True
                break
            start += 1
            end += 1
    return isperm
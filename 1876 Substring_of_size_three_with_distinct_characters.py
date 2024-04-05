def countGoodSubstrings(self, s: str) -> int:
    start = 0 
    end = start +3
    count = 0
    while end < len(s)+1:
        hasht = {}
        for i in s[start:end]:
            hasht[i] = 1+ hasht.get(i,0)
        if(all(x < 2 for x in list(hasht.values()))):
            count +=1
        start+=1
        end+=1
    return count
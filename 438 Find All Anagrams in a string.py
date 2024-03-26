def findAnagrams(self, s: str, p: str) -> List[int]:
    
    if len(p) > len(s):
        return []
    start = 0
    end = len(p)
    answer = []
    shash,phash = {},{}
    for i in range(len(p)):
        phash[p[i]] = 1 + phash.get(p[i],0)
        shash[s[i]] = 1 + shash.get(s[i],0)

   
    return answer



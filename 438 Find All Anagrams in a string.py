def findAnagrams(self, s: str, p: str) -> List[int]:
    # use sliding algorithm 
    # in addition to that store the elements occurence in a hashtable 
    # in order to compare the two strings
    if len(p) > len(s):
        return []
    start = 0
    end = len(p)
    answer = []
    shash,phash = {},{}
    for i in range(len(p)):
        phash[p[i]] = 1 + phash.get(p[i],0)
        shash[s[i]] = 1 + shash.get(s[i],0)

    if shash == phash:
        answer.append(0)
    for i in range(len(s)-len(p)):
        # print(shash,phash,start,end,"-------")
        shash[s[end]] = 1 + shash.get(s[end],0)
        if (shash[s[start]] == 1):
            shash.pop(s[start])
        else:
            shash[s[start]] -= 1
        if (shash == phash):
            answer.append(i+1)
        start +=1 
        end +=1 
    return answer



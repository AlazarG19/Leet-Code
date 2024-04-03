def uniqueLetterString(self, s: str) -> int:
    listcount = {}
    for i in range(len(s)):
        if listcount.get(s[i]) == None:
            listcount[s[i]] = [i]
        else:
            listcount[s[i]].append(i)
    totalcount = 0
    for individualcount in listcount:
        listcount[individualcount].insert(0,-1)
        listcount[individualcount].insert(len(s)+1,len(s))
        for j in range(1,len(listcount[individualcount])-1):
            left = listcount[individualcount][j] - listcount[individualcount][j-1]
            right = listcount[individualcount][j+1] - listcount[individualcount][j]
            count = left*right
            totalcount += count
    return totalcount
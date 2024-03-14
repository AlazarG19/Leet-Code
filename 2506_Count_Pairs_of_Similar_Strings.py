def similarPairs(self, words: List[str]) -> int:
    output = 0
    for i in range(len(words)):
        for j in range(i+1,len(words)):
            if(set(words[i]) == set(words[j])):
                output += 1
    return output
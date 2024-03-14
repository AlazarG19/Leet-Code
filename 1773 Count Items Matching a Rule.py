def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
    matching = 0
    for i in items:
        if ruleKey == "color":
            if(i[1] == ruleValue):
                matching += 1
        elif ruleKey == "type":
            if(i[0] == ruleValue):
                matching += 1
        if ruleKey == "name":
            if(i[2] == ruleValue):
                matching += 1
    return matching

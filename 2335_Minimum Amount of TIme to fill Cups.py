def fillCups(self, amount: List[int]) -> int:
    result = 0
    while True:
        amount = [x for x in amount if x >0]
        if(len(amount) == 0):
            break
        elif(len(amount) == 1):
            result += amount[0]
            break
        else:
            result +=1
            if len(amount) > 2:
                amount.sort(reverse=True)
                amount = [x-1 for x in amount[0:2] if x >0] + amount[2:]
            else:
                amount.sort(reverse=True)
                amount = [x-1 for x in amount if x >0]
    return result

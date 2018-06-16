def pickingNumbers(a):
    dicNumCount = {}
    for x in a:
        if x in dicNumCount:
            dicNumCount[x] += 1
        else:
            dicNumCount[x] = 1
    
    maxCount = -1
    for x in dicNumCount:
        countwithPrev = dicNumCount[x] + (dicNumCount[x-1] if (x-1) in dicNumCount else 0)
        countwithNext = dicNumCount[x] + (dicNumCount[x+1] if (x+1) in dicNumCount else 0)
        if countwithNext > maxCount and countwithNext > countwithPrev:
            maxCount = countwithNext
        else:
            if countwithPrev > maxCount:
                maxCount = countwithPrev

    return maxCount


print(pickingNumbers([1, 2, 2, 3, 1, 2]))
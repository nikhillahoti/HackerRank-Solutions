
def get_rock_quantity(quantity):
    jamie = quantity
    ned = sorted(quantity)

    dictCount = {}
    dictIndex = {}

    counter = len(quantity)
    for i in range(0,counter):
        total = jamie[i] + ned[i]
        if total in dictCount:
            dictCount[total] = dictCount[total] + 1
        else:
            dictCount[total] = 1
        dictIndex[total] = i

    finalKey = list(dictCount.keys())[0]
    finalcount = dictCount[finalKey]

    for key in dictCount:
        if dictCount[key] > finalcount:
            finalKey = key
            finalcount = dictCount[key]
        else:
            if key > finalKey and dictCount[key] == finalcount:
                finalKey = key

    return dictIndex[finalKey]

print(get_rock_quantity([1,2,6]))
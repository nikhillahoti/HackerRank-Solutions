
def birthdayCakeCandles(ar):
    maxCount = 1
    maxElem = ar[0]

    i = 1
    counter = len(ar)
    while i < counter:
        if ar[i] > maxElem:
            maxElem = ar[i]
            maxCount = 1
        else:
            if ar[i] == maxElem:
                maxCount = maxCount + 1

        i = i + 1

    return  maxCount

print(birthdayCakeCandles([3, 1, 2, 3]))
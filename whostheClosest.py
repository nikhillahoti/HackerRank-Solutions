dict = [[] for i in range(26)]

for i in range(len(s)):
    dict[ord(s[i]) - 97].append(i)

def getLocation(element, itslocation):
    lst = dict[ord(element) - 97][:]
    #lst.remove(itslocation)
    if len(lst) <= 1:
        return -1
    else:
        low = 0
        high = len(lst) - 1
        mid = 0
        while low <= high:
            mid = (low + high) / 2

            if lst[mid] == itslocation:
                break
            if itslocation > lst[mid]:
                low = mid + 1
            else:
                high = mid - 1

        if mid == 0:
            return lst[1]

        if mid == len(lst) - 1:
            return lst[len(lst) - 2]

        return lst[mid + 1] if (lst[mid + 1] - itslocation) < (itslocation - lst[mid - 1]) else lst[mid - 1]


output = []
for i in range(len(queries)):
    output.append(getLocation(s[queries[i]], queries[i]))
return output

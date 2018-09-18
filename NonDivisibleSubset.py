
def nonDivisibleSubset(k, S):
    counter = len(S)
    if counter < 1:
        return 0
    
    remainder = [0] * k
    for i in range(0, counter):
        remainder[S[i] % k] = remainder[S[i] % k] + 1

    final = 0
    counter = int(k//2+1)
    S = set([(x,k-x) for x in range(1,counter)])
    for i,j in S:
        if i != j:
            if remainder[i] > remainder[j]:
                final  = final + remainder[i]
            else:
                final = final + remainder[j]
        else:
            if remainder[i] > 0:
                final = final + 1
    if remainder[0] > 0:
        final = final + 1
    return final 

S = [1, 7, 2, 6, 8, 5, 15, 16, 18, 19, 25, 12, 14]
k = 5
print(nonDivisibleSubset(k, S))



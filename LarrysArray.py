
def larrysArray(A):
    A = [0] + A
    counter = len(A)

    def findIndex(A, i):
        for j in range(i, counter):
            if A[j] == i: return j
        return -1

    def RotateElem(A, curr, right):

        if curr > right - 2:
            temp = A[curr]
            A[curr] = A[curr + 1]
            A[curr + 1] = A[curr + 2]
            A[curr + 2] = temp
        else:
            SwapElems(A, right - 2)
        if A[curr] == curr: return
        RotateElem(A, curr, right - 2)

    def SwapElems(A, index):
        temp = A[index]
        A[index] = A[index + 2]
        A[index + 2] = A[index + 1]
        A[index + 1] = temp

    counter2 = counter - 2
    for left in range(1, counter2):
        if A[left] == left: continue
        index = findIndex(A, left)
        RotateElem(A, left, index)

    if sorted(A) == A: return  "YES"
    return  "NO"

#A = [1, 3, 4, 2]
A = [1, 6, 5, 2, 4, 3]
A = [3, 1, 2]
A = [1, 2, 3, 5, 4]
print(larrysArray(A))




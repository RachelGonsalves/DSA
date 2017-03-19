def mergesort(A):
    n = len(A)

    if(n<2):
        return

    mid = n//2
    left = A[0:mid]
    right = A[mid:n]

    mergesort(left)
    mergesort(right)
    merge(left, right,A)

    return A

def merge(L,R,A) :
    nL = len(L)
    nR = len(R)
    i = 0
    j = 0
    k = 0

    while(i< nL and j<nR):
        if (L[i] <= R[j]):
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1

    while(i<nL) :
        A[k] = L[i]
        i += 1
        k += 1

    while(j<nR) :
        A[k] = R[j]
        j += 1
        k += 1



B = [-1, 22, 7, 104, 0, 54, 1, 62]
print(mergesort(B))
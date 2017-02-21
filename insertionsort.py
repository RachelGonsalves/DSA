def insertion(A):
    n = len(A)
    for i in range(1,n):
        hole = i
        value = A[i]

        while (hole>0 and A[hole-1]>value):
            A[hole] = A[hole-1]
            hole -= 1

        A[hole] = value

    return A

A = [2,88,9,0,7]
print(insertion(A))

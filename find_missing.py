def missing_number(A, B):
    a = []
    if A == B:
        return 0

    if A != B:
        for i in A:
            if i not in B:
                a.append(i)
        for j in B:
            if j not in A:
                a.append(j)
    return a

print missing_number([1, 2, 3, 4], [1 ,2, 3])
print missing_number([1], [1])
print missing_number([],[])
